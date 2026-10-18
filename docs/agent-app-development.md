# STEPX Neo 原生 Agent App 开发说明：MCP、A2A 与 HTTP/WebSocket 怎么选

> 适用对象：要在 STEPX Neo 上做一个「能被 Amoo 调用」或「自己就是一个 Agent」的原生应用。
> 本文结论基于本机能力清单（360 项原子能力）的实际字段，以及平台上已接入的第三方 Agent（支付宝、剪映、微信）的调用形态；标注为「平台接入文档为准」的部分，请以官方最新模板校验。

## 一、先给结论

三条路线不是三选一，而是三层：

| 层次 | 用什么 | 解决什么 | 典型场景 |
|---|---|---|---|
| 能力层 | **MCP / AppFunctions** | 把 App 的功能变成助手可发现、可调用的「工具」 | 打开页面、查数据、写记录、发消息 |
| 协作层 | **A2A（JSON-RPC 会话）** | 把一整件事委托给一个有自己推理循环的 Agent | 一句话成片、跨步骤代办、多轮澄清 |
| 传输层 | **HTTP / WebSocket** | App 与自家后端通信 | 同步数据、推消息、拉配置 |

一句话选择法：

- **只想被调用** → MCP（Android 上就是 AppFunctions），不要自己造协议。
- **自己带 Agent、要流式与产物** → A2A；底层传输仍是 JSON-RPC 帧，不是裸 WebSocket 自定义协议。
- **只服务自家 UI / 自家后端** → HTTP/WS 随便用，但助手发现不了你，也拿不到权限与卡片能力。

多数「Agent App」最终是 **MCP + A2A 叠加**：用 MCP 暴露细粒度操作，用 A2A 承接需要多轮推理的整体任务。

## 二、为什么不是「直接 HTTP / WebSocket」

如果目标是让 Amoo 能调用你的 App，裸 HTTP/WS 会缺四样东西：

1. **发现机制**：助手怎么知道你有什么能力、参数是什么；
2. **权限与确认**：哪些能力需要用户点头、哪些属于敏感操作；
3. **执行位置语义**：端侧执行还是云端执行，数据出不出设备；
4. **结果承载**：结构化结果、卡片渲染、失败与重试语义。

这四样正好是能力注册表（MCP schema）和 A2A 会话层负责的部分。WebSocket 只是字节通道，把这些重新发明一遍，既拿不到系统级权限，也不会出现在能力清单里。

> 例外：纯后台同步、推送、长连接信令，用 HTTP/WS 完全合理——但它们是「App 内部实现」，不是「Agent 接入协议」。

## 三、MCP / AppFunctions：把 App 变成设备端工具服务器

### 3.1 它在 Android 上是什么

AppFunctions 是 Android 16+ 的平台能力（配 Jetpack 库），本质是**设备端 MCP**：应用把内部函数注册进系统函数表，助手或其它被授权的调用方按 schema 发现并执行，全程走本地 IPC，不依赖网络往返。

对应到 STEPX Neo 的能力清单，这类能力长这样：

- `callType = FUNCTION_CALL` 或 `MCP`
- `callingMethod = LOCAL`
- `authType = APP_SIGN`
- `functionName` 形如 `com.stepos.weather.appfunctions.WeatherFunctions#get_current_location_weather`
- `extra` 里带 `jetpackSchemaVersion`、`jetpackParametersJson`、`jetpackResponseJson`

清单里共有 9 项这种形态（天气、相机、应用商店等），另有 345 项以 MCP 形态登记，298 项为端侧执行。

### 3.2 最小骨架（Kotlin）

```kotlin
// 入参 / 出参：必须是可序列化类型，KDoc 会被解析成给模型看的描述
@AppFunctionSerializable
data class AddTodoArgs(
    /** 待办标题，必填，例如「周五交周报」 */
    val title: String,
    /** 截止时间，ISO 8601；不传表示无截止 */
    val dueAt: String? = null
)

@AppFunctionSerializable
data class AddTodoResult(
    /** 新建待办的唯一 id */
    val id: String,
    /** 是否创建成功 */
    val ok: Boolean
)

class TodoFunctions : AppFunctionService() {

    @AppFunction(isDescribedByKDoc = true)
    suspend fun addTodo(args: AddTodoArgs): AddTodoResult {
        // 只做一件事，保持幂等；耗时操作自行加超时
        val id = repository.insert(args.title, args.dueAt)
        return AddTodoResult(id = id, ok = true)
    }
}
```

Manifest 需要注册由 KSP 生成的 `AppFunctionService` 子类；调用方需持有 `EXECUTE_APP_FUNCTIONS` 权限（具体权限名与注册方式以当前 Android/平台模板为准）。

### 3.3 设计要点

- **一个函数一件事**：`addTodo` 比 `doEverything` 更容易被正确选择；负面样例写进 KDoc，能显著降低误调用。
- **schema 即契约**：参数名、必填项、取值范围要写清楚，模型只看这些。
- **短调用**：单次调用控制在秒级；长任务拆成 `start` + `status` 两个函数，或改用 A2A。
- **端侧优先**：能本地做的不要上云，`LOCAL + APP_SIGN` 的信任成本最低。
- **失败要可读**：返回结构化错误码 + 人话原因，别只抛异常。

## 四、A2A：把整件事委托给另一个 Agent

### 4.1 适用判断

满足任意两条，就该考虑 A2A：

- 你的 App 内有自己的规划 / 推理循环；
- 任务需要多轮澄清或流式进度；
- 产出是文件、图片、视频等「产物」，不是一次性结构化结果；
- 需要保持会话上下文（同一件事的多次调用）。

### 4.2 平台上的实际形态

平台对三方 Agent 的统一承载方式是：**一个代理原子能力 + 一层会话信封**，例如：

- 支付宝：`proxy_third_party_ability_alipay_xui_service` / `..._alipay_mcp_service`
- 剪映：`proxy_third_party_ability_capcut_creation`
- 微信：`proxy_third_party_ability_wechat_voice_control`

共同特征：

1. 入参固定为 `target`、`payload`、`timeout`；
2. `payload` 是**编码后的会话报文**（支付宝是 A2A JSON-RPC 字节流的 base64；剪映是 JSON 信封字符串）；
3. 必须有 **conversation / contextId** 贯穿多轮；
4. 返回是**帧序列**，最后一帧才是终态；附带执行状态、错误码、产物 URI；
5. 超时有明确业务码（如剪映 `16001`），超时不等于任务失败，需要续查或补领。

剪映信封示例（形态参考）：

```json
{
  "op": "send",
  "conversation_id": "",
  "payload": { "text": "把这三张照片剪成 15 秒的旅行 vlog" }
}
```

下行帧（形态参考）：

```json
{ "action": "progress", "status": "running", "err_code": 0, "data": "正在挑选片段" }
{ "action": "final", "status": "ok", "err_code": 0, "artifacts": [{ "uri": "content://..." }] }
```

支付宝 A2A 形态则是标准 JSON-RPC：`params.message.contextId` 必须非空且稳定，Token 位置由平台在握手时注入，调用方不要自带凭证。

### 4.3 关键约束

- **会话 id 自建且复用**：同一件事的多轮必须复用同一个 `conversation_id` / `contextId`，否则对方会当成新任务。
- **超时是常态**：设计成「发出去 → 轮询/等帧 → 收产物」，不要假设一次调用就能拿到终态。
- **幂等**：同一请求重发不能产生两笔真实业务（下单、支付、发布）。
- **产物走 URI**：不要把二进制塞进返回体；用平台给的资源 URI，并按需申请临时读权限。
- **明确停手条件**：用户取消、连续失败、超出预算，都要能 `cancel` 并释放会话。

## 五、能力清单里能看到的字段（开发自检用）

| 字段 | 对开发者的含义 |
|---|---|
| `name` / `toolUniqueName` | 调用名与唯一标识（`appId_方法_版本号`）；改名等于新能力 |
| `callType` | `MCP` / `FUNCTION_CALL` / `API`，决定调用通道 |
| `callingMethod` | `LOCAL` 端侧执行 / `CLOUD` 云端执行 |
| `authType` | `APP_SIGN` 表示需要应用签名校验的端侧调用 |
| `inputSchema` / `outputSchema` | JSON Schema，调用方唯一可信的参数来源 |
| `slaScene` / `pendingApproval` | 是否需要用户确认或属于敏感场景 |
| `extra` 中的 `jetpack*` | 该能力由 AppFunctions 声明，说明是端侧函数形态 |

自检方法：改完代码后拉一次能力清单，确认新能力出现在列表里且 schema 正确；不要靠「代码里写了」判断已注册。

## 六、推荐落地路径

**第一步（1～2 天）：只做 MCP**
挑 3～5 个高频、边界清晰的操作注册成 AppFunctions，跑通「用户说一句话 → 助手选对你的函数 → 端侧执行 → 结构化返回」。这一步能覆盖 80% 的接入价值。

**第二步（按需）：加 A2A**
当出现「需要你的 App 自己规划多步」的场景，再接 A2A：定义会话 id、帧协议、超时与取消、产物回传。不要把已有 MCP 函数重新包一层 A2A，除非确实需要多轮推理。

**第三步：再考虑传输优化**
只有在自建后端、长连接推送、大文件传输时，才引入 HTTP/WS；并且让它待在 App 内部，不暴露给助手。

## 七、常见坑

1. **用 WebSocket 自造协议对接助手**：发现不了、没权限、卡片不渲染，最后还是要回到能力注册。
2. **一个函数干太多事**：模型选不准，失败也难定位；按动词拆分。
3. **把长任务塞进单次 MCP 调用**：超时后状态丢失，用户看到「失败了」但实际已执行。
4. **会话 id 每次新建**：多轮上下文断裂，对方反复澄清同一件事。
5. **忽略用户确认**：涉及支付、下单、删除、发送等动作，必须走确认；`pendingApproval` / `slaScene` 不是装饰。
6. **返回大对象**：schema 里塞整页 HTML 或 base64，既慢又容易被截断；返回 id + 摘要，详情另查。
7. **只测成功路径**：超时、重复调用、权限被拒、对方 Agent 返回中间态，都要有明确处理。

## 八、验收清单

- [ ] 能力出现在清单中，`name`、`inputSchema`、`callingMethod` 均符合预期
- [ ] 正常路径：一句话触发、参数正确、结果可读
- [ ] 异常路径：缺参、超时、权限拒绝、重复调用均有确定行为
- [ ] 长任务：可查询进度、可取消、产物可取回
- [ ] 敏感操作：有用户确认，且确认前不产生真实副作用
- [ ] 权限最小化：不申请与功能无关的系统权限
- [ ] 无网络时端侧能力仍可用（若声明为 `LOCAL`）

## 九、FAQ

**Q：能不能只用 A2A，不用 MCP？**
可以，但你会失去细粒度工具的可发现性。A2A 更适合「整件事委托」，MCP 更适合「单步操作」；两者叠加最自然。

**Q：能不能只用 MCP，不用 A2A？**
大多数工具型 App 都够用。只有当你的 App 需要自己规划多步、流式输出或产出文件时，才需要 A2A。

**Q：WebSocket 能不能做流式？**
能，但那是你和自家后端的流；对助手暴露的流式，应通过 A2A 的帧序列表达，否则平台无法统一处理超时、取消与产物。

**Q：云端执行（CLOUD）什么时候用？**
需要跨设备、依赖服务端模型或数据时；端侧能完成的尽量留在 `LOCAL`，权限与隐私成本都更低。

---

*本文与 `data/abilities.json` 同步维护；能力清单更新后，字段含义以最新快照为准。*
