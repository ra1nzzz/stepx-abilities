#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 data/abilities.json 重新生成 README.md 与 docs/abilities-by-app.md。

用法：
    python3 scripts/render.py

只依赖标准库。快照内容指纹（content_sha256_16）变化即代表设备能力有更新。
"""
import collections
import datetime
import hashlib
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "abilities.json")
TRUNC = 160


def load():
    if not os.path.exists(SRC):
        raise SystemExit("缺少 data/abilities.json，无法渲染")
    data = json.load(open(SRC, encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("data") or []
    return data


def clean(text):
    s = (text or "").replace("|", "\\|")
    s = re.sub(r"#\s*description", "", s)
    s = re.sub(r"#\s*positive_samples", "｜正例：", s)
    s = re.sub(r"#\s*negative_samples", "｜反例：", s)
    s = re.sub(r"#\s*return", "｜返回：", s)
    s = re.sub(r"#\s*params?", "｜参数：", s)
    s = re.sub(r"\s*\n\s*", " ", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" ·｜")


def truncate(text, limit=TRUNC):
    return text if len(text) <= limit else text[:limit] + "…"


def group(items):
    counter = collections.Counter(x.get("appName") or "未知" for x in items)
    grouped = collections.OrderedDict()
    for app, _ in counter.most_common():
        grouped[app] = sorted(
            [x for x in items if (x.get("appName") or "未知") == app],
            key=lambda x: x.get("name") or "",
        )
    return grouped


def fingerprint(items):
    blob = json.dumps(items, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


def render():
    items = load()
    grouped = group(items)
    total = len(items)
    local = sum(1 for x in items if (x.get("callingMethod") or "").upper() == "LOCAL")
    cloud = sum(1 for x in items if (x.get("callingMethod") or "").upper() == "CLOUD")
    rev = fingerprint(items)

    snap_path = os.path.join(ROOT, "data", "snapshot.json")
    gen_at = None
    if os.path.exists(snap_path):
        try:
            gen_at = json.load(open(snap_path, encoding="utf-8")).get("generated_at")
        except Exception:
            gen_at = None
    if not gen_at:
        gen_at = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=8))
        ).isoformat(timespec="seconds")
        json.dump(
            {
                "generated_at": gen_at,
                "device": "STEPX Neo",
                "total": total,
                "local": local,
                "cloud": cloud,
                "apps": len(grouped),
                "content_sha256_16": rev,
            },
            open(snap_path, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2,
        )

    stamp = gen_at.replace("T", " ")[:16]
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)

    # ---------- 明细 ----------
    lines = [
        "# 原子能力明细（按 App 分组）\n",
        f"快照时间：{stamp}（UTC+8）　·　共 {total} 项能力 / {len(grouped)} 个 App\n",
        "> 入参 / 出参的完整 JSON Schema 见 `data/abilities.json`。\n",
        "---\n",
    ]
    for app, rows in grouped.items():
        pkg = next((r.get("packageName") for r in rows if r.get("packageName")), None)
        desc = next((r.get("appDesc") for r in rows if r.get("appDesc")), "")
        meta = f"`{pkg}`" if pkg else "云端服务"
        head = f"{meta}　·　{len(rows)} 项能力"
        if desc:
            head += f"　·　{clean(desc)}"
        lines.append(f"## {app}\n")
        lines.append(head + "\n")
        lines.append("| 能力 | 说明 | 执行 | 鉴权 |")
        lines.append("|---|---|---|---|")
        for r in rows:
            lines.append(
                "| `{}` | {} | {} | {} |".format(
                    r.get("name") or "-",
                    truncate(clean(r.get("description"))),
                    r.get("callingMethod") or "-",
                    r.get("authType") or "-",
                )
            )
        lines.append("")
    open(os.path.join(ROOT, "docs", "abilities-by-app.md"), "w", encoding="utf-8").write(
        "\n".join(lines)
    )

    # ---------- README ----------
    index_rows = "\n".join(
        f"| [{app}](#{app}) | {len(rows)} |" for app, rows in grouped.items()
    )
    readme = f"""# STEPX Neo 原子能力清单

STEPX Neo 设备上**已注册原子能力（ability）的全量清单**，由设备侧能力注册表导出整理，用于能力检索、版本对账和接入前的可行性确认。

> 快照时间：**{stamp}（UTC+8）**　·　能力总数：**{total}**　·　覆盖 App/服务：**{len(grouped)}**　·　内容指纹：`{rev}`

## 清单概况

| 指标 | 数值 |
|---|---|
| 能力总数 | {total} |
| 本机执行（LOCAL） | {local} |
| 云端执行（CLOUD） | {cloud} |
| 覆盖 App / 服务 | {len(grouped)} |

## 文件说明

| 路径 | 内容 |
|---|---|
| `docs/abilities-by-app.md` | 按 App 分组的可读明细（能力名、说明、执行方式、鉴权） |
| `data/abilities.json` | 原始快照（完整字段，含入参/出参 Schema） |
| `data/snapshot.json` | 快照元信息（时间、总数、内容指纹） |
| `scripts/render.py` | 由原始快照重新生成 README 与明细 |
| `docs/agent-app-development.md` | 原生 Agent App 开发说明：MCP / A2A / HTTP 与 WebSocket 的取舍 |

## 相关文档

- [原生 Agent App 开发说明](docs/agent-app-development.md)：MCP（AppFunctions）、A2A 与裸 HTTP/WebSocket 分别解决什么问题，以及推荐落地路径。

## App 索引

| App / 服务 | 能力数 |
|---|---|
{index_rows}

## 字段说明

| 字段 | 含义 |
|---|---|
| `name` | 能力方法名，调用时使用 |
| `toolUniqueName` | 能力唯一标识（`appId_方法_版本号`） |
| `appName` / `packageName` | 所属 App 与包名 |
| `description` | 能力说明，部分为 Markdown |
| `callingMethod` | `LOCAL` 端侧执行 / `CLOUD` 云端执行 |
| `authType` | 鉴权方式，如 `APP_SIGN` |
| `inputSchema` / `outputSchema` | 入参 / 出参 JSON Schema |
| `slaScene` / `pendingApproval` | SLA 场景 / 是否需要人工确认 |

## 使用说明

- 清单随设备能力版本变化，`content_sha256_16` 用于比对版本是否更新。
- 调用参数以 `inputSchema` 为准，不要臆造字段名。
- 标注 `pendingApproval` 的能力可能触发用户确认，属预期行为。
- 重新生成：`python3 scripts/render.py`。
"""
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(readme)
    print(f"OK total={total} apps={len(grouped)} local={local} cloud={cloud} rev={rev}")


if __name__ == "__main__":
    render()
