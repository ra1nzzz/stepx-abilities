# 原子能力明细（按 App 分组）

快照时间：2026-10-30 09:04（UTC+8）　·　共 381 项能力 / 38 个 App

> 入参 / 出参的完整 JSON Schema 见 `data/abilities.json`。

---

## 设置

`com.android.settings`　·　56 项能力　·　手机系统设置项查询及管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `settings_adjust_brightness` | 调整屏幕亮度（无需进入显示设置），支持两种方式： 1. 相对调节：传 openState（true=调亮一些，false=调暗一些）。 2. 绝对设置：传 newValue（1~100 的百分比，超出取最大/最小），将亮度设为指定百分比。 两者按需二选一：需要“设为具体百分比”时用 newValue，需要“调亮/调暗一… | LOCAL | APP_SIGN |
| `settings_adjust_font_size` | 直接调整系统字体大小（无需进入显示设置）。 ｜正例： - 把字体调大一点 - 调小字体 - 字体太小了，调大些 - 把字体改小 ｜反例： - 打开字体设置页面 → 暂时不支持 ｜返回： 返回字符串，字体改大： - 已改大：返回"字体改小：" - 已该小：返回"字体已改小" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_adjust_sound` | 直接调整音量（无需进入设置），支持媒体音量与铃声音量： - 用 openState 控制增大(true)/减小(false)。 - 用 soundType 指定对象：不传或 media=媒体音量；ring=铃声音量。 涉及“铃声/来电铃声”时传 soundType=ring，其它默认媒体音量。 ｜正例： - 调大音量 … | LOCAL | APP_SIGN |
| `settings_airplane_mode_switch` | 直接开启或关闭飞行模式（无需进入设置）。 ｜正例： - 打开飞行模式 - 帮我开一下飞行模式 - 关闭飞行模式 - 把飞行模式关掉 | LOCAL | APP_SIGN |
| `settings_app_lock_config_switch` | 直接开启或关闭应用锁/应用加密，直接打开应用锁界面/应用加密界面。 ｜正例： - 帮我开启应用锁 - 关闭应用加密 - 把应用锁打开 - 把应用加密关掉 | LOCAL | APP_SIGN |
| `settings_auto_brightness_switch` | 直接开启或关闭自动亮度调节。 ｜正例： - 开启自动亮度 - 关闭自动亮度 - 打开自适应亮度 - 把亮度改成自动调节 | LOCAL | APP_SIGN |
| `settings_auto_rotation_switch` | 直接开启或关闭屏幕自动旋转。 ｜正例： - 打开自动旋转 - 关闭自动旋转 - 屏幕不要转 - 横屏竖屏自动切换 - 方向锁定 | LOCAL | APP_SIGN |
| `settings_battery_percentage_switch` | 直接显示或隐藏状态栏电池电量百分比。 ｜正例： - 显示电量百分比 - 把状态栏电池百分比打开 - 隐藏电量数字 - 关闭电池电量百分比显示 | LOCAL | APP_SIGN |
| `settings_battery_saver_switch` | 直接开启或关闭省电模式。 ｜正例： - 帮我开启省电模式 - 关闭省电模式 - 打开节能模式 - 把省电关了 | LOCAL | APP_SIGN |
| `settings_bluetooth_switch` | 直接开启或关闭蓝牙。 ｜正例： - 打开蓝牙 - 关闭蓝牙 - 把蓝牙打开 - 把蓝牙关掉 ｜反例： - 打开蓝牙设置页 → 应走 | LOCAL | APP_SIGN |
| `settings_charging_notif_sound_switch` | 直接开启或关闭充电提示音和振动。 ｜正例： - 开启充电提示音 - 关掉充电提示音 - 打开充电振动 - 关闭充电提示音和振动 | LOCAL | APP_SIGN |
| `settings_choose_wifi` | 在已保存的 WiFi 网络之间切换连接到指定 WiFi。 正文中的 WiFi 名称/SSID 等可能被加密，为PII密文令牌[[PII:SEC1.{keyID}.{epk}.{ct}]]（keyID与epk、ct均为动态；epk/ct为URL-safe Base64，可含-和_），保持原样透传即可，不要向用户索要明文。… | LOCAL | APP_SIGN |
| `settings_dark_mode_switch` | 直接开启或关闭系统深色模式。 ｜正例： - 打开深色模式 - 关闭深色模式 - 开启暗黑模式 - 关掉夜间模式 | LOCAL | APP_SIGN |
| `settings_data_switch` | 直接开启或关闭蜂窝数据网络。 ｜正例： - 打开流量 - 关闭流量 - 开数据 - 关掉移动数据 - 打开蜂窝数据 ｜反例： - 打开移动网络设置页面 → 应走 connectivitysettings_open_settings_mobile_network_settings_activity | LOCAL | APP_SIGN |
| `settings_dialing_keypad_sound_switch` | 直接开启或关闭拨号键盘提示音。 ｜正例： - 开启拨号提示音 - 关闭拨号按键音 - 把拨号键盘声音打开 - 把拨号键盘提示音关掉 | LOCAL | APP_SIGN |
| `settings_disturb_mode_switch` | 直接开启或关闭勿扰模式。 ｜正例： - 开启勿扰模式 - 关闭勿扰模式 - 打开免打扰 - 关掉勿扰 | LOCAL | APP_SIGN |
| `settings_eye_protection_mode_switch` | 直接开启或关闭护眼模式（夜间显示）。 ｜正例： - 打开护眼模式 - 关闭护眼模式 - 开启夜间护眼 - 关掉护眼 ｜返回： 返回字符串，描述开启结果，包含护眼模式当前状态： - 已开启：返回"护眼模式开启" - 已关闭：返回"护眼模式关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_forget_wifi` | 根据 WiFi 名称删除或忘记已保存的 WiFi 网络。 正文中的 WiFi 名称/SSID 等可能被加密，为PII密文令牌[[PII:SEC1.{keyID}.{epk}.{ct}]]（keyID与epk、ct均为动态；epk/ct为URL-safe Base64，可含-和_），保持原样透传即可，不要向用户索要明文。… | LOCAL | APP_SIGN |
| `settings_get_airplane_mode_state` | 查询飞行模式的开关状态（无需进入设置）。 ｜正例： - 飞行模式开了吗 - 查询飞行模式状态 - 当前是否在飞行模式 ｜返回： 返回字符串，描述查询结果，包含飞行模式当前状态： - 已开启：返回"飞行模式开启" - 已关闭：返回"飞行模式关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_app_lock_state` | 查询应用锁或应用加密的开关状态。 ｜正例： - 应用锁开了吗 - 查一下应用加密状态 - 帮我看看应用锁开关状态 ｜返回： 返回字符串，描述查询结果，包含应用锁（应用加密）当前状态： - 已开启：返回"应用锁开启" - 已关闭：返回"应用锁关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_auto_brightness_state` | 查询自动亮度调节的开关状态。 ｜正例： - 自动亮度开了吗 - 查一下自适应亮度状态 - 帮我看看自动亮度调节是不是开着 ｜返回： 返回字符串，描述查询结果，包含自动亮度当前状态： - 已开启：返回"自动调节亮度开启" - 已关闭：返回"自动调节亮度关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_auto_rotation_state` | 查询屏幕自动旋转开关状态。 ｜正例： - 自动旋转开了吗 - 帮我查一下屏幕旋转状态 - 看看自动旋转现在是不是打开的 ｜返回： 返回字符串，描述查询结果，包含屏幕自动旋转当前状态： - 已开启：返回"自动旋转屏幕开启" - 已关闭：返回"自动旋转屏幕关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_battery_percentage_state` | 查询电池电量百分比显示的开关状态。 ｜正例： - 电量百分比开了吗 - 电池百分比状态是什么 - 查一下电量百分比显示状态 ｜返回： 返回字符串，描述查询结果，包含状态栏电池电量百分比显示开关当前状态： - 已开启：返回"电量百分比开启" - 已关闭：返回"电量百分比关闭" - 查询失败：返回"Query Error.… | LOCAL | APP_SIGN |
| `settings_get_battery_saver_state` | 查询省电模式的开关状态。 ｜正例： - 省电模式开了吗 - 现在是否在省电模式 - 查一下省电开关状态 ｜返回： 返回字符串，描述查询结果，包含省电模式当前状态： - 已开启：返回"省电模式开启" - 已关闭：返回"省电模式关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_bluetooth_state` | 查询蓝牙开关状态。 ｜正例： - 蓝牙开了吗 - 查一下蓝牙状态 - 帮我看看蓝牙开关是不是开着 ｜反例： - 打开已连接设备里的蓝牙页面 → 应走 connectivitysettings_open_settings_bluetooth_settings_activity ｜返回： 返回字符串，描述查询结果，包含蓝牙… | LOCAL | APP_SIGN |
| `settings_get_charging_notif_sound_state` | 查询充电提示音和振动的开关状态。 ｜正例： - 充电提示音开了吗 - 帮我查一下充电振动状态 - 查充电提示开关 ｜返回： 返回字符串，描述查询结果，包含充电提示音开关当前状态： - 已开启：返回"充电提示音开启" - 已关闭：返回"充电提示音关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_current_battery_level` | 查询设备当前实际的电池电量百分比。返回的是电量数值本身（例如 "75%"），不是开关状态。 ｜正例： - 现在电量多少 - 我还有多少电 - 剩多少电 - 电量是多少 - 电池百分之多少 - 现在还剩几格电 ｜反例： - 电量百分比显示开了吗 → 应走 settings_get_battery_percentage_s… | LOCAL | APP_SIGN |
| `settings_get_dark_mode_state` | 查询深色模式开关状态。 ｜正例： - 深色模式开了吗 - 暗黑模式状态是什么 - 查一下深色模式 ｜返回： 返回字符串，描述查询结果，包含深色模式当前状态： - 已开启：返回"深色模式开启" - 已关闭：返回"深色模式关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_data_state` | 查询数据网络（流量）开关状态。 ｜正例： - 流量开了吗 - 帮我查一下移动数据状态 - 查数据网络开关状态 ｜返回： 返回字符串，描述查询结果，包含移动数据网络开关当前状态： - 已开启：返回"移动数据开启" - 已关闭：返回"移动数据关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_dialing_keypad_sound_state` | 查询拨号键盘提示音开关状态。 ｜正例： - 拨号按键音开了吗 - 查一下拨号提示音状态 - 帮我看看拨号声音有没有开启 ｜返回： 返回字符串，描述查询结果，包含拨号键盘按键音开关当前状态： - 已开启：返回"拨号键盘按键音开启" - 已关闭：返回"拨号键盘按键音关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_hotspot_state` | 查询个人热点开关状态。 ｜正例： - 热点开了吗 - 热点状态是什么 - 查一下热点开关 ｜反例： - 打开热点设置页面 → 应走 connectivitysettings_open_settings_tether_settings_activity ｜返回： 返回字符串，描述查询结果，包含个人热点开关当前状态： - … | LOCAL | APP_SIGN |
| `settings_get_liftToCheck_phone_state` | 获取“闭拿起手机即显示”的开关状态，获取“抬起唤醒”的开关状态。查询类的原子能力，无需进入显示页面。 | LOCAL | APP_SIGN |
| `settings_get_one_handed_mode_state` | 查询单手模式开关状态。 ｜正例： - 单手模式开了吗？ - 帮我查一下单手模式开关状态。 ｜返回： 返回字符串，描述查询结果，包含单手模式当前状态： - 已开启：返回"单手模式开启" - 已关闭：返回"单手模式关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_screen_lock_sound_state` | 查询屏幕锁定提示音开关状态。 ｜正例： - 锁屏音开了吗 - 锁屏提示音状态 - 查锁屏声音 ｜返回： 返回字符串，描述查询结果，包含锁屏提示音开关当前状态： - 已开启：返回"锁屏提示音开启" - 已关闭：返回"锁屏提示音关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_tapToCheck_phone_state` | 获取“双击亮屏”的开关状态，获取“双击亮屏”的开关状态。查询类的原子能力，无需进入显示页面。 | LOCAL | APP_SIGN |
| `settings_get_touch_sound_state` | 查询点按/点击提示音开关状态。 ｜正例： - 点按提示音开了吗 - 查一下点击音状态 - 帮我看看点按声音有没有打开 ｜返回： 返回字符串，描述查询结果，包含点按提示音（触摸音效）开关当前状态： - 已开启：返回"触摸提示音开启" - 已关闭：返回"触摸提示音关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_vibration_state` | 查询系统震动开关状态。 ｜正例： - 振动开了吗 - 帮我查一下震动状态 - 查振动开关 ｜返回： 返回字符串，描述查询结果，包含来电震动开关当前状态： - 已开启：返回"来电震动开启" - 已关闭：返回"来电震动关闭" - 查询失败：返回"Query Error." | LOCAL | APP_SIGN |
| `settings_get_wifi_state` | 查询 WiFi 开关状态。 ｜正例： - WiFi 开了吗？ - 帮我查一下 WiFi 开关状态 - 现在 WiFi 是开着的吗？ ｜反例： - 打开 WiFi 设置页面 → 应走 connectivitysettings_open_settings_advanced_wifi_settings_activity - … | LOCAL | APP_SIGN |
| `settings_hotspot_switch` | 直接开启或关闭个人热点。 ｜正例： - 打开热点 - 关闭热点 - 开个人热点 - 关热点 - 共享网络 ｜反例： - 打开热点设置入口 → 应走 connectivitysettings_open_settings_tether_settings_activity | LOCAL | APP_SIGN |
| `settings_liftToCheck_phone_switch` | 打开/关闭拿起手机即显示功能，打开/关闭抬起亮屏功能，打开/关闭抬起唤醒功能。开关类的原子能力，可以快速更新“拿起手机即显示”开关的状态，以满足用户的日常使用。优先调用该原子能力，不要模拟调用。 | LOCAL | APP_SIGN |
| `settings_one_handed_mode_switch` | 直接开启或关闭单手模式。 ｜正例： - 打开单手模式 - 关闭单手模式 - 开启单手操作 | LOCAL | APP_SIGN |
| `settings_open_feedback` | 打开帮助和反馈首页。不要打开选择反馈分类。 ｜正例： - 打开帮助和反馈 - 进入帮助和反馈 - 打开帮助与反馈 ｜反例： - 选择反馈分类 → 不要打开这一页 - 我要提交问题反馈 → 应走 feedback_submit_question - 打开设置主页 → 应走 settings_open_settings_h… | LOCAL | APP_SIGN |
| `settings_open_language` | 打开语言和输入法页面。说打开输入法设置就进这一页。 ｜正例： - 打开输入法设置 - 打开语言和输入法 - 进入语言和输入法 ｜反例： - 打开设置主页 → 应走 settings_open_settings_homepage_activity - 只切换系统语言 → 应走 settings_adjust_system… | LOCAL | APP_SIGN |
| `settings_open_manage_applications` | 打开所有应用页面。它显示所有已安装的应用。此页面允许您查看所有已安装的应用。 | LOCAL | APP_SIGN |
| `settings_open_settings_device_info_settings_activity` | 打开/进入“关于本机”界面。此界面显示手机型号、系统版本号以及设备标识符（IP 地址、MAC 地址、蓝牙地址等）等信息。 | LOCAL | APP_SIGN |
| `settings_open_settings_homepage_activity` | 打开系统设置主页面。 ｜正例： - 打开设置 - 进入系统设置 - 打开手机设置 - 去设置主页 ｜反例： - 打开网络设置 → 应走 connectivitysettings_open_settings_wireless_settings_activity - 进入 SIM 卡设置 → 应走 connectivity… | LOCAL | APP_SIGN |
| `settings_open_settings_locale_picker_activity` | 打开/进入语言设置界面。此功能不会直接调整系统语言。 | LOCAL | APP_SIGN |
| `settings_open_settings_sound_settings_activity` | 打开/进入音量页面。打开音量管理页面。该功能不直接打开音量的开关，该页面包含显示音量，振动及勿扰模式及手机铃声等设置项。 ｜正例： - 打开音量设置 - 进入音量管理页面 - 帮我打开声音和振动设置页面 - 我想调手机铃声，打开相关设置 | LOCAL | APP_SIGN |
| `settings_open_settings_storage_dashboard_activity` | 打开/进入存储空间界面。该界面主要展示了存储空间使用量的显示以及存储空间管理。 ｜正例： - 打开存储空间 - 进入手机存储空间界面 - 查看存储空间使用情况 - 打开存储空间管理 | LOCAL | APP_SIGN |
| `settings_screen_lock_sound_switch` | 打开屏幕锁定提示音，关闭屏幕锁定提示音，开关类的原子能力，无需进入对应页面，可以直接开启或关闭屏幕锁定提示音。 ｜正例： - 打开屏幕锁定提示音 - 关闭屏幕锁定提示音 - 帮我开启锁屏提示音 - 把锁屏提示音关掉 | LOCAL | APP_SIGN |
| `settings_set_media_sound` | 将设备的媒体音量调整到用户指定的百分比水平。 ｜正例： - 把媒体音量调到百分之五十 - 把视频声音调小到百分之二十 - 把媒体声音调到百分之八十 | LOCAL | APP_SIGN |
| `settings_set_screen_off_time` | 调整系统自动锁屏/息屏时间，支持两种方式： 1. 设为固定时间：传 newValue（单位秒，用户以分钟表达时换算为秒）。 2. 相对调节：传 openState（true=延长/调长，false=缩短/调短），在系统档位间上下调一档。 需要“设为具体时长”时用 newValue，需要“调长/调短一点”时用 openS… | LOCAL | APP_SIGN |
| `settings_tapToCheck_phone_switch` | 打开/关闭“双击亮屏”（双击亮屏）。开关类的原子能力，可以快速更新“双击亮屏”开关的状态，以满足用户的日常使用。优先调用该原子能力，不要模拟调用。 | LOCAL | APP_SIGN |
| `settings_touch_sound_switch` | 打开点按和点击提示音，关闭点按和点击提示音，开关类的原子能力，无需进入对应页面，可以直接开启或关闭点按和点击提示音。 ｜正例： - 打开点按和点击提示音 - 关闭点按和点击提示音 - 把点击提示音打开 - 关掉点按提示音 | LOCAL | APP_SIGN |
| `settings_vibration_switch` | 打开系统震动，关闭系统震动，开关类的原子能力，无需进入显示页面，可以直接打开或关闭系统震动。 ｜正例： - 打开系统震动 - 关闭系统震动 - 把手机震动开一下 - 关掉系统震动 | LOCAL | APP_SIGN |
| `settings_wifi_switch` | 直接开启或关闭本机 WiFi（WLAN）开关，在设备本地生效，无需进入设置页面。关闭 WiFi 可能中断当前网络连接及依赖该连接的任务；开启 WiFi 仅表示启用无线功能，不保证已连接 WiFi 网络或互联网可用。正常返回时，以本次调用结果为准。仅当「关闭 WiFi」调用超时、没有拿到结果时：不要重复下发关闭，也不要挂… | LOCAL | APP_SIGN |

## 图库

`com.stepos.media.gallery`　·　48 项能力　·　查看、管理照片及视频

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `gallery_add_picture_filter` | 在图库中为图片套用预设滤镜，可选类型：亮度(brightness)、对比度(contrast)、双色调(duotone)、鱼眼(fisheye)、染色(tint)。 ｜正例： - 给这张图加个滤镜 - 帮这张照片换个滤镜风格 - 把这张照片调成双色调 - 给这张图套个鱼眼效果 - 给这张图加点染色效果 ｜反例： - 打… | LOCAL | APP_SIGN |
| `gallery_add_picture_mosaic` | 在图库中对指定区域打**马赛克**，支持多块；块大小建议 30~80（绝对像素，过小看不出），类型可为块状或图片式（字段 block/image）。**区域可用两种方式之一指定**：(A) 语义位置 `position+size`（适合"右下角"、"中心"等模糊定位）；(B) 像素坐标 `x+y+width+heigh… | LOCAL | APP_SIGN |
| `gallery_add_picture_text` | 在图库中给指定图片叠加文字，并支持配置文字位置、颜色、字号、粗体和旋转等样式。 ｜正例： - 给这张图上加字 - 给照片加个标题 - 在图片上标注一段文字 - 给这张图配一句话 ｜反例： - 给这张图片加水印防盗 → 应走 gallery_add_picture_watermark - 在图上用画笔圈出重点 → 应走 … | LOCAL | APP_SIGN |
| `gallery_add_picture_watermark` | 在图库中为图片添加水印，支持配置水印文案、颜色、大小、位置、角度等样式。 ｜正例： - 给这张图片加个水印 - 把这张图打上水印 - 给图片加防盗图标记 - 在照片左上角加上水印文案 ｜反例： - 给这张照片加一行普通标题文字 → 应走 gallery_add_picture_text # examples - 给照片… | LOCAL | APP_SIGN |
| `gallery_ai_erase_image` | 在图库中打开编辑并直接进入 **AI 消除**，路径支持本地绝对路径及 file://、content://。 ｜正例： - 帮我把这张照片里的路人消除掉 - 去掉图片里的杂物 - 把圈选区域的内容抹掉 - AI 消除这张图的瑕疵 - 帮我把水印擦掉 ｜反例： - 打开这张图片的完整编辑页，我自己修 → 应走 gall… | LOCAL | APP_SIGN |
| `gallery_ai_extend_image` | 在图库中打开编辑并直接进入 **AI 扩图**，路径支持本地绝对路径及 file://、content://。 ｜正例： - 帮我把这张图做 AI 扩图 - 把这张照片往外延展一下 - 补全这张图的画面边缘 - 这张图太窄了，帮我加宽 - 给这张图生成更多背景 ｜反例： - 打开这张图片的完整编辑页，我自己修 → 应走… | LOCAL | APP_SIGN |
| `gallery_ai_style_image` | 在图库中打开编辑并直接进入 **AI 风格/妙绘**，路径支持本地绝对路径及 file://、content://。 ｜正例： - 给这张照片做 AI 风格化 - 帮我把这张图变成动漫风 - 用 AI 妙绘改一下这张图 - 给图片换个艺术风格 - 做 AI 写真风格 ｜反例： - 打开这张图片的完整编辑页，我自己修 →… | LOCAL | APP_SIGN |
| `gallery_compress_media` | 在图库中压缩图片或视频，可设置压缩质量，输出路径以端侧为准。 ｜正例： - 帮我压缩这张图片 - 把这个视频压小一点 - 减小这张图的文件体积 - 降低画质省点空间 | LOCAL | APP_SIGN |
| `gallery_copy_files_to_album` | 在图库中将用户指定的多个文件复制到指定目标相册。 ｜正例： - 把这些文件复制到目标相册 - 把选中的图片拷贝到宝宝相册 - 把这些图复制到旅行相册 | LOCAL | APP_SIGN |
| `gallery_copy_media` | 在图库或存储中将指定媒体复制到目标路径，生成一份副本。 ｜正例： - 把这张照片复制一份到目标文件夹 - 把这个视频备份到我指定的目录 - 给这份媒体另存一份到别处 - 把这个文件拷贝到目标路径 | LOCAL | APP_SIGN |
| `gallery_create_album` | 在图库中新建一个自定义名称的相册。 ｜正例： - 帮我新建一个相册 - 在图库里创建一个旅行相册 - 加一个新的宝宝相册 | LOCAL | APP_SIGN |
| `gallery_edit_picture_aspect_ratio` | 在图库中按指定固定长宽比例对图片进行中心裁剪，支持 1:1、4:3、16:9、3:4、9:16。 ｜正例： - 把这张图裁成正方形 - 把这张照片裁成 16:9 - 按比例中心裁剪这张图片 - 把图片裁成竖屏 9:16 - 把这张照片裁成头像 1:1 ｜反例： - 打开这张图的完整编辑页，我自己来裁剪 → 应走 gal… | LOCAL | APP_SIGN |
| `gallery_edit_picture_brightness` | 在图库中调节图片亮度，取值约 -255～255，负值偏暗、正值偏亮。 ｜正例： - 把这张照片调亮一点 - 这张图太暗了，帮我提亮 - 把照片调暗一些 - 这张图片亮度不够，弄亮些 ｜反例： - 打开图片编辑器，我自己调亮度 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_edit_picture_degree` | 在图库中将图片按指定角度顺时针旋转，支持 90°、180° 或 270°。 ｜正例： - 把这张照片顺时针旋转90度 - 这张图倒过来了，帮我转正 - 把这张歪了的图转一下 - 把照片旋转180度 | LOCAL | APP_SIGN |
| `gallery_edit_picture_flip` | 在图库中对图片进行翻转，方向支持水平左右镜像或垂直上下镜像。 ｜正例： - 把这张图左右镜像一下 - 给当前照片做水平翻转 - 把图片上下翻转 - 把这张图上下颠倒 ｜反例： - 打开图片编辑器，我自己来翻转这张图 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_edit_picture_paint` | 在图库中使用画笔在图片上涂鸦或标注，并可配置笔刷粗细与颜色。 ｜正例： - 用画笔在这张图上圈出重点 - 在图片上画条线标出来 - 给这张照片涂鸦标记一下 - 用红色画笔在图上做个手绘标注 ｜反例： - 在图片上加一段文字标注 → 应走 gallery_add_picture_text - 给这张图打个水印标记 → 应… | LOCAL | APP_SIGN |
| `gallery_edit_picture_saturation` | 在图库中调节图片饱和度，1.0 为原图，小于 1 偏灰，大于 1 偏艳。 ｜正例： - 把这张图颜色调淡一点 - 这张照片太艳了，降饱和 - 把照片调得鲜艳一点 - 这张图灰蒙蒙的，调艳一点 ｜反例： - 打开这张图的编辑器，我自己调色 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_edit_picture_sharpen` | 在图库中对指定图片进行锐化处理，并按给定强度增强图片清晰度。 ｜正例： - 把这张照片锐化一下 - 让这张图更清晰一点 - 把这张照片的边缘处理清楚些 - 这张照片有点发虚，帮我加强细节 ｜反例： - 打开这张图片的编辑页，我想自己调整锐化 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_edit_picture_temperature` | 在图库中调节指定图片的色温，负值偏冷色调，正值偏暖色调。 ｜正例： - 把这张照片的色温调冷一点 - 这张图太黄了，帮我调一下色温 - 把照片调成暖色氛围 - 给这张图片加一点冷色调 ｜反例： - 打开这张照片的完整编辑器让我自己调色 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_favorite_media` | 在图库中对指定媒体执行收藏或取消收藏操作。 ｜正例： - 收藏这张图 - 把这段视频加到收藏 - 取消收藏这张照片 - 从收藏里去掉这个视频 | LOCAL | APP_SIGN |
| `gallery_get_latest_media` | 在图库中获取本地**最新创建**的一张图片或一段视频的完整路径，无则为空；可选媒体类型为视频或图片（字段值 image/video），默认图片。 ｜正例： - 最新照片在哪 - 帮我找刚拍的那张图 - 刚保存的视频给我 - 找出本地最新媒体 ｜反例： - 找最近三天拍的照片 → 应走 gallery_get_media… | LOCAL | APP_SIGN |
| `gallery_get_local_stickers` | 在图库中获取本机已保存的贴纸，并可限制最多返回数量。 ｜正例： - 查看我的本地贴纸 - 找一下我抠图保存的贴纸 - 看看我自己存的贴纸 - 获取离线保存的贴纸 | LOCAL | APP_SIGN |
| `gallery_get_media_by_time_range` | 在图库中按起止时间检索图片或视频，时间格式为年-月-日 时:分:秒，须按**真实当前时间**推算勿抄示例日期；可选视频或图片类型。 ｜正例： - 找一下最近三天拍的照片 - 帮我查这周的照片 - 找上个月拍的视频 - 按日期找一下相册里的图片 - 搜一下某段时间图库里的视频 ｜反例： - 找图库里最新的一张图片 → 应… | LOCAL | APP_SIGN |
| `gallery_get_photo_info` | 在图库中读取单张图片的元数据，包括宽高、大小、文件名、拍摄时间、相机型号、焦距、ISO、光圈、快门、GPS 等，以实际返回为准。 ｜正例： - 查一下这张照片的拍摄参数 - 这张照片是什么相机拍的 - 这张图片分辨率多少 - 看看这张照片有没有定位信息 - 这张照片文件多大 | LOCAL | APP_SIGN |
| `gallery_get_sticker_columns` | 在图库中获取贴纸分类列表，可按最大返回类目数限制结果。 ｜正例： - 图库里的贴纸有哪些分类？ - 帮我看看贴纸栏目有哪些 - 贴纸商城有哪些大类？ - 有哪些贴纸包分类？ | LOCAL | APP_SIGN |
| `gallery_get_stickers` | 在图库中按贴纸类目编号批量获取贴纸资源，可指定单次获取最大数量。 ｜正例： - 帮我获取这个贴纸类目里的贴纸列表 - 把这几个贴纸分类里的贴纸素材一起拉取出来 - 按贴纸栏目编号拿贴纸资源 | LOCAL | APP_SIGN |
| `gallery_get_style_templates` | 在图库中获取风格迁移或风格化模板列表，可限制返回的最大模板数量。 ｜正例： - 帮我看看图库里有哪些艺术风格模板 - 获取一下风格化模板列表 - 图库里有什么换画风的模板 - 给我列出油画风格模板 | LOCAL | APP_SIGN |
| `gallery_get_trash_media_list` | 获取图库回收站中的媒体文件列表。 ｜正例： - 查看图库回收站里的照片和视频 - 帮我看看相册回收站有哪些文件 - 获取回收站中的媒体文件列表 | LOCAL | APP_SIGN |
| `gallery_get_video_info` | 在图库中读取指定单段视频的元数据，包括宽高、大小、文件名、时长、码率、采样率等，以实际返回为准。 ｜正例： - 这视频多长？ - 帮我查一下这段视频的大小 - 看看这个视频的码率是多少 - 查一下这段片子的分辨率 | LOCAL | APP_SIGN |
| `gallery_hide_album` | 在图库中隐藏指定相册，使其在相册列表中不可见。 ｜正例： - 帮我隐藏这个相册 - 把这个相册设为不显示 - 不想让别人看到这个相册 - 把这个相簿收起来 | LOCAL | APP_SIGN |
| `gallery_hide_media` | 在图库中隐藏指定单条媒体，使其不在图库列表中展示。 ｜正例： - 隐藏这张照片 - 别在相册里显示这张图 - 把这张图片藏起来 - 这张单图设为私密 | LOCAL | APP_SIGN |
| `gallery_intelligent_search` | 在图库中用自然语言对本地相册进行语义智能搜索，支持泛化类别词，并可限制最多返回条数。 ｜正例： - 帮我找海边的照片 - 找有猫的图片 - 相册里日落那张 - 智能搜图 - 用话描述找视频 ｜反例： - 找最近拍的照片 → 应走 gallery_get_media_by_time_range - 获取最新创建的一张图片… | LOCAL | APP_SIGN |
| `gallery_local_search` | 在图库中基于本地索引按时间、地点、人物、相册、场景、OCR 文字等条件组合搜索图片或视频，兼容通用关键词搜索，同字段取并集、不同字段取交集。 ｜正例： - 找上周旅游的照片 - 搜微信截图里的订单图 - 查某个人在海边的照片 - 找带某段文字的截图 ｜反例： - 找最近几天拍的照片 → 应走 gallery_get_m… | LOCAL | APP_SIGN |
| `gallery_move_media_to_album` | 在图库中将单条媒体文件移动到指定目标相册，相册不存在时常会自动创建。 ｜正例： - 把这张图移到旅行相册 - 把这段视频归类到宝宝册 - 把当前这张照片换到另一个相册存放 - 把这张图片整理到指定相册 | LOCAL | APP_SIGN |
| `gallery_move_to_folder` | 在图库中将指定文件按路径移动到目标文件夹。 ｜正例： - 把这张照片移到目标文件夹 - 将这个视频挪到指定文件夹 - 帮我把这个文件换个目录存放 | LOCAL | APP_SIGN |
| `gallery_open_hidden_album` | 在图库中**打开隐藏相册**页面，查看已隐藏的媒体文件。 ｜正例： - 帮我打开隐藏相册 - 查看私密照片 - 我要找隐藏的图 - 私密相册在哪 - 看看被隐藏的照片 | LOCAL | APP_SIGN |
| `gallery_open_picture_editor` | 在图库中打开指定图片的完整图片编辑页，供用户继续裁剪、调色等编辑操作。 ｜正例： - 打开这张图片的编辑器 - 我要修这张图 - 用图库编辑这张照片 - 进入图片的完整编辑页 ｜反例： - 打开这张图的 AI 扩图 → 应走 gallery_ai_extend_image - 帮我把路人消除掉 → 应走 gallery… | LOCAL | APP_SIGN |
| `gallery_open_trash_bin` | 在图库中**打开回收站**页面，查看已删除的媒体文件。 ｜正例： - 打开回收站 - 去回收站看看 - 查看已删除的照片 - 我要恢复文件 - 被删的图在哪 | LOCAL | APP_SIGN |
| `gallery_open_video_editor` | 在图库中打开视频剪辑并载入指定视频。 ｜正例： - 剪这个视频 - 打开视频编辑 - 我要剪这段录像 ｜反例： - 打开图片编辑，修这张图 → 应走 gallery_open_picture_editor | LOCAL | APP_SIGN |
| `gallery_open_video_player` | 在图库中用播放器播放指定路径的视频。 ｜正例： - 播放这个视频 - 打开这段录像看看 - 预览一下这段视频 - 全屏播放这个视频 | LOCAL | APP_SIGN |
| `gallery_reduce_picture_resolution` | 在图库中降低指定图片的分辨率，用于压缩体积或适配上传。 ｜正例： - 把这张图片分辨率调低一点 - 这张图太大了，帮我压小点 - 把图片像素降一点 - 降低这张照片的分辨率方便上传 | LOCAL | APP_SIGN |
| `gallery_rename_album` | 在图库中将指定相册由旧名称重命名为新名称。 ｜正例： - 把相册“旧相册”重命名为“新相册” - 帮我把这个相册换个名字 - 把相簿名称从“旧名称”改成“新名称” | LOCAL | APP_SIGN |
| `gallery_rename_media` | 在图库中重命名图片或视频文件，新文件名可不带后缀。 ｜正例： - 把这张照片重命名 - 给这个视频换个名字 - 把这张图的文件名改一下 - 别用默认名，给这张照片改名 | LOCAL | APP_SIGN |
| `gallery_restore_media_from_trash` | 从图库回收站恢复一个或多个媒体文件。 ｜正例： - 把回收站里的这些照片恢复回来 - 恢复我刚才删掉的那几个视频 - 把图库回收站里选中的媒体文件还原 | LOCAL | APP_SIGN |
| `gallery_select_media_file_card` | 在图库中打开**媒体选择卡片**，让用户勾选本地图片或视频；类型可选仅图、仅视频或全部（image/video/all），返回所选路径等。 ｜正例： - 帮我从相册里选照片 - 打开选图界面 - 我要从图库里多选几张图片 - 让我自己选图片 - 从相册里挑视频素材 | LOCAL | APP_SIGN |
| `gallery_set_album_cover` | 在图库中将指定相册的封面设置为指定图片。 ｜正例： - 把旅行相册的封面换成这张图 - 用这张照片当相册封面 - 帮我把这个相册的封面图设一下 | LOCAL | APP_SIGN |
| `gallery_share_media` | 在图库中调起系统分享，将指定路径的图片或视频分享给其他应用。 ｜正例： - 分享这张照片 - 把这个视频发给其他应用 - 用系统分享把这张图发出去 - 发微信 | LOCAL | APP_SIGN |
| `gallery_unhide_media` | 在图库中取消隐藏指定媒体文件，使其恢复在相册中显示。 ｜正例： - 把这张图取消隐藏 - 让这段视频重新显示在相册里 - 把这个媒体文件恢复显示 - 别藏这张照片了，显示回来 | LOCAL | APP_SIGN |

## 通用原子能力

`com.stepos.common.ability.proxy`　·　45 项能力　·　提供系统通用能力，应用开启及卸载、文件上传、获取设备及系统信息等

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `batch_file_upload` | 上传本地文件到服务端（批量），适用于只需要发起批量上传、不要求一次性返回全部文件结果或实时进度的场景。 ｜正例： - 上传文件 - 把这些文件传上去 - 批量上传这些文件 ｜反例： - 批量上传文件并一次性返回所有上传结果 → 应走 batch_file_upload_return_all - 批量上传这些文件并实时显… | LOCAL | APP_SIGN |
| `batch_file_upload_all_progress` | 批量上传本地文件，并通过 progressToken 实时返回上传进度。适用于需要展示上传百分比、监听状态变化或处理单个文件失败原因的场景。 ｜正例： - 上传文件看进度 - 批量上传并监听进度 - 显示上传百分比 ｜反例： - 批量上传这些文件 → 应走 batch_file_upload - 批量上传文件并一次性返… | LOCAL | APP_SIGN |
| `batch_file_upload_return_all` | 批量上传本地文件，并在全部文件处理完成后一次性返回所有上传结果。适用于只关心最终结果、不需要实时进度的场景。 ｜正例： - 批量上传文件 - 上传一批文件并拿到结果 - 把这些本地文件都上传并返回结果 ｜反例： - 批量上传文件并显示上传进度 → 应走 batch_file_upload_all_progress - … | LOCAL | APP_SIGN |
| `check_app_installed_by_name` | 通过应用显示名称检查指定应用是否已安装。当前按系统应用列表中的显示名称忽略大小写匹配：优先完全匹配，未命中时按显示名前缀匹配以兼容简称（如“携程”命中“携程旅行”）；仍未命中时返回 false。 ｜正例： - 看看我手机上装没装微信 - 帮我查一下有没有安装淘宝 - 确认一下抖音是不是已安装 ｜反例： - 通过包名检查… | LOCAL | APP_SIGN |
| `check_app_installed_by_package` | 通过 Android 应用包名检查对应应用是否已安装。包名为空时返回参数错误；包名合法但设备上不存在时返回 false。 ｜正例： - 检查 com.tencent.mm 这个包名装没装 - 查一下包名 com.example.app 的应用有没有安装 - 帮我看看这个 packageName 对应的应用是否已安装 ｜… | LOCAL | APP_SIGN |
| `clear_back_screen_frame` | 清除刚刚通过 set_back_screen_frame 下发的自定义点阵，退出自定义帧模式并恢复当前 agent 状态显示。没有自定义帧时调用也安全。 ｜正例： - 清掉背屏上刚画的图案 - 取消副屏自定义显示 - 恢复背屏原来的 agent 动画 ｜反例： - 推送一张新的自定义点阵 → 应走 set_back_s… | LOCAL | APP_SIGN |
| `common_ability_check_app_permission` | 按应用包名和 Android 权限常量检查应用是否拥有指定权限。permissionName 应使用 android.permission.CAMERA、android.permission.RECORD_AUDIO、android.permission.ACCESS_FINE_LOCATION 等系统权限名；不建议直… | LOCAL | APP_SIGN |
| `common_ability_clipboard_text` | 获取系统剪贴板中的文本内容。仅用于读取文本类型内容；剪贴板为空、当前内容不是文本或系统限制读取时，按实际读取结果返回空文本或错误信息。 ｜正例： - 剪贴板文字是什么 - 复制的内容是什么 - 读一下剪贴板文字 ｜反例： - 复制这段文字到剪贴板 → 不应走本能力 - 清空剪贴板 → 不应走本能力 | LOCAL | APP_SIGN |
| `common_ability_get_app_count` | 获取当前手机已安装的第三方应用总个数，不包含系统预装应用。适用于用户只关心第三方应用数量、不需要完整应用列表的场景。 ｜正例： - 装了多少个第三方应用 - 已安装 app 有几个 - 第三方应用数量是多少 ｜反例： - 列出已安装的第三方应用 → 应走 common_ability_get_app_list - 检查… | LOCAL | APP_SIGN |
| `common_ability_get_app_list` | 获取当前手机已安装的第三方应用列表，返回应用名称和包名等信息。不包含系统预装应用。适用于用户想查看设备上安装了哪些第三方应用的场景。 ｜正例： - 列出已安装的第三方应用 - 看看装了哪些 app - 获取第三方应用列表 ｜反例： - 获取已安装应用数量 → 应走 common_ability_get_app_coun… | LOCAL | APP_SIGN |
| `common_ability_get_app_permissions` | 按应用包名获取应用的非普通权限使用详情，包括位置、相机、麦克风等敏感权限的授权状态或使用信息。适用于查看指定包名应用的权限列表和权限使用详情。 ｜正例： - 查看这个应用的权限列表 - 这个应用用了哪些权限 - 查看指定包名应用的权限使用详情 ｜反例： - 检查应用是否有某一个权限 → 应走 common_abilit… | LOCAL | APP_SIGN |
| `common_ability_get_app_versioncode` | 根据 Android 应用包名获取指定已安装应用的 versionCode。包名为空时返回参数错误；应用未安装或查询失败时按实现返回错误或 -1。 ｜正例： - 获取 com.tencent.mm 的 versionCode - 查下指定包名应用的版本号 - 帮我查一下某个应用包名的 versionCode ｜反例： … | LOCAL | APP_SIGN |
| `common_ability_get_screen_size` | 获取当前手机屏幕的完整物理分辨率，包括屏幕宽度和高度，单位为像素 px。 ｜正例： - 屏幕多大 - 我手机屏幕尺寸是多少 - 屏幕分辨率是多少 - 屏幕宽高是多少 ｜反例： - 调整屏幕分辨率 → 不应走本能力 - 修改屏幕缩放比例 → 不应走本能力 | LOCAL | APP_SIGN |
| `common_ability_has_face_rec` | 查询当前手机硬件是否支持人脸识别功能。只判断设备能力支持情况，不代表当前已录入人脸或已开启人脸解锁。 ｜正例： - 手机支不支持人脸识别 - 能用刷脸吗 - 支持面部识别吗 - 可以刷脸解锁吗 ｜反例： - 设置人脸解锁 → 不应走本能力 - 录入人脸信息 → 不应走本能力 | LOCAL | APP_SIGN |
| `common_ability_has_fingerprint` | 查询当前手机硬件是否支持指纹识别功能。只判断设备能力支持情况，不代表当前已录入指纹或已开启指纹解锁。 ｜正例： - 手机有指纹吗 - 支持指纹识别吗 - 能指纹解锁吗 - 指纹功能支持不 ｜反例： - 设置指纹解锁 → 不应走本能力 - 录入新的指纹 → 不应走本能力 | LOCAL | APP_SIGN |
| `get_back_screen_auto_brightness` | 查询背屏自动背光开关是否打开。只读，不修改设置。 ｜正例： - 背屏自动亮度开着吗 - 副屏是不是自动背光 ｜反例： - 打开/关闭背屏自动背光 → 应走 set_back_screen_auto_brightness - 查询/调节手动亮度 → 应走 get_back_screen_brightness / set_… | LOCAL | APP_SIGN |
| `get_back_screen_auto_rotate` | 查询背屏横竖屏适配（自动旋转）开关是否打开。 ｜正例： - 背屏会不会自动旋转 - 副屏横竖屏适配开着吗 ｜反例： - 打开/关闭横竖屏适配 → 应走 set_back_screen_auto_rotate | LOCAL | APP_SIGN |
| `get_back_screen_basic_type` | 查询背屏待机显示类型：agent 默认动画、time 时间、text 自定义文本。类型为 text 时同时返回当前文本。 ｜正例： - 背屏待机显示的是什么 - 副屏现在是时钟还是自定义文字 ｜反例： - 改成时间 / 自定义文字 → 应走 set_back_screen_basic_type | LOCAL | APP_SIGN |
| `get_back_screen_brightness` | 查询背屏手动亮度，范围为 1–255。返回的是已存储的手动档；若自动背光开着，该值暂不作用于面板。 ｜正例： - 背屏亮度是多少 - 副屏手动亮度调到几了 ｜反例： - 把背屏调亮/调暗 → 应走 set_back_screen_brightness - 打开/关闭自动背光 → 应走 set_back_screen_a… | LOCAL | APP_SIGN |
| `get_back_screen_camera_link` | 查询背屏相机联动开关是否打开。打开时占用相机可在背屏显示相机相关状态。 ｜正例： - 背屏相机联动开了吗 - 副屏拍照联动是不是开着 ｜反例： - 打开/关闭相机联动 → 应走 set_back_screen_camera_link | LOCAL | APP_SIGN |
| `get_back_screen_display_info` | 查询背屏当前显示信息，包含亮灭状态（Display.state）、逻辑宽高、旋转角度、当前亮度。只读，不修改任何设置。 ｜正例： - 背屏现在亮着吗 - 查一下副屏宽高和亮度 - 背屏当前状态是什么 ｜反例： - 点亮/熄灭背屏 → 应走 wake_up_back_screen / sleep_back_screen … | LOCAL | APP_SIGN |
| `get_back_screen_display_mode` | 查询背屏显示模式：auto 智能显示、always 始终显示、custom 定时显示，并返回定时窗口起止（距午夜的分钟数及时钟时间）。 ｜正例： - 背屏现在是智能显示还是常亮 - 副屏定时亮屏从几点到几点 ｜反例： - 改成始终显示 / 定时显示 → 应走 set_back_screen_display_mode -… | LOCAL | APP_SIGN |
| `get_back_screen_enabled` | 查询手机背屏（副屏）总开关当前是否打开。只读状态，不修改任何设置。 ｜正例： - 背屏开着吗 - 副屏现在是开还是关 - 查一下背屏开关状态 ｜反例： - 打开/关闭背屏 → 应走 set_back_screen_enabled - 背屏亮度是多少 → 不应走本能力 | LOCAL | APP_SIGN |
| `open_app_by_name` | 根据应用显示名称打开应用，可选传入 Activity class name 打开具体 Activity。当前按系统应用列表中的显示名称忽略大小写匹配：优先完全匹配，未命中时按显示名前缀匹配以兼容简称（如“携程”命中“携程旅行”），多个命中时取显示名最短者；未找到应用、无默认启动入口或指定 Activity 启动失败时返… | LOCAL | APP_SIGN |
| `open_app_by_package` | 根据 Android 应用包名打开应用；仅传 packageName 时启动该应用的默认入口 Activity，同时传 packageName 与 className 时直接启动指定 Activity。适用于用户明确提供包名或需要打开指定包名 Activity 的场景。 ｜正例： - 按包名打开应用 - 启动 com.… | LOCAL | APP_SIGN |
| `open_url_with_browser` | 打开浏览器应用，并传入 URL 打开具体网页。url 必须以 http:// 或 https:// 开头；不支持缺少协议的地址、file:// 或本地路径。 ｜正例： - 用浏览器打开 https://www.baidu.com/ - 打开这个网页链接 - 帮我在浏览器里打开 URL ｜反例： - 打开浏览器应用 → … | LOCAL | APP_SIGN |
| `proxy_third_party_ability_alipay_life_service` | 支付宝「服务直达」原子能力入口 —— 覆盖智跃星辰服务直达 P0 场景，让用户在**支付宝**内 完成以下明确范围的生活服务。 ## 高频强支持意图（命中即强路由到本能力，勿让给地图/POI/外卖等其它 agent） 以下两类是高频核心场景，**只要 query 命中（含出现在复合 query 的任一子句里）就必须强路… | LOCAL | APP_SIGN |
| `proxy_third_party_ability_alipay_mcp_service` | 支付宝「对话内闭环」原子能力入口 —— 支付宝下发卡片，**卡片直接渲染在助手对话内、全程不跳转 支付宝**，用户在卡片上选规格 / 确认订单后由调用方回传，形成「推荐 → 下单 → 履约·核销状态查询」 的多轮闭环。 ## 优先级：本能力最高，命中即强路由 本能力覆盖的场景，与支付宝 xUI 服务执行（`proxy_… | LOCAL | APP_SIGN |
| `proxy_third_party_ability_alipay_xui_service` | 支付宝 xUI「服务执行」原子能力入口 ｜返回： 返回 [AlipayXuiServiceResult]：`code=0`（且 `_meta.metas` 中 `executionState=COMPLETED`）为执行成功； 10001/10002/10003/10004 入参非法（10004 为缺少有效 `para… | LOCAL | APP_SIGN |
| `proxy_third_party_ability_capcut_creation` | 剪映（CapCut）AI 创作原子能力入口 —— 让用户用一句话，由**剪映**创作 Agent 完成视频 / 图片 / 音乐等短视频创作，并把成片 / 草稿产物回传。命中以下创作意图时云端应路由到本能力，由剪映侧 创作 Agent 完成精准的创作模式判定与素材编排，工具层负责与剪映 App 建立会话、上传本地素材、 … | LOCAL | APP_SIGN |
| `proxy_third_party_ability_wechat_voice_control` | 微信语音控制原子能力。Amoo 将用户原始语音以 16kHz/单声道/PCM16 传入，由微信完成联系人识别、 消息内容理解、确认 UI 和消息/音视频电话执行。本能力按 contextId 维持多轮 OVC Session；返回的 content 应由 Amoo 使用 TTS 播报。只适用于发微信消息、微信语音电话和… | LOCAL | APP_SIGN |
| `set_back_screen_auto_brightness` | 打开或关闭背屏自动背光。打开后按环境光自动调节；关闭后使用手动亮度。 ｜正例： - 打开背屏自动亮度 - 关掉副屏自动背光 ｜反例： - 查询自动背光状态 → 应走 get_back_screen_auto_brightness - 把背屏调亮/调暗到具体数值 → 应走 set_back_screen_brightne… | LOCAL | APP_SIGN |
| `set_back_screen_auto_rotate` | 打开或关闭背屏横竖屏适配。打开后主屏亮起时背屏跟随设备姿态旋转。 ｜正例： - 打开背屏自动旋转 - 关掉副屏横竖屏适配 ｜反例： - 查询横竖屏适配状态 → 应走 get_back_screen_auto_rotate | LOCAL | APP_SIGN |
| `set_back_screen_basic_type` | 设置背屏待机显示。type=agent 默认动画，time 时间，text 自定义文本。选 text 时必须同时传 text。内置字库仅支持大写 A-Z、数字 0-9 以及 ! - ? 空格共 40 个字符（小写会自动转大写）。含中文时本能力会改走 set_back_screen_frame 点阵显示，最多 6 个字。… | LOCAL | APP_SIGN |
| `set_back_screen_brightness` | 设置背屏手动亮度，范围为 1–255。设置时会自动关闭自动背光，使该值立即生效。面板在 1、2 档时观感与 3 档相同，调用方无需自行抬底。 ｜正例： - 把背屏亮度调到 128 - 副屏调亮一点到 200 - 背屏亮度设为最暗 ｜反例： - 查询当前亮度 → 应走 get_back_screen_brightness… | LOCAL | APP_SIGN |
| `set_back_screen_camera_link` | 打开或关闭背屏相机联动。打开后占用相机时背屏可显示相机图标等状态；关闭会清掉硬件占用的相机 SPECIAL 槽。 ｜正例： - 打开背屏相机联动 - 关闭副屏拍照联动 ｜反例： - 查询相机联动状态 → 应走 get_back_screen_camera_link - 打开相机应用 → 应走 open_app_by_n… | LOCAL | APP_SIGN |
| `set_back_screen_display_mode` | 设置背屏显示模式。auto=智能显示（事件点亮后超时熄灭），always=始终显示，custom=定时显示（窗口内常亮，窗外等同智能显示）。定时显示可同时传 customStart / customEnd，单位是距午夜的分钟数，例如早上 8 点为 8×60=480，晚上 22 点为 1320。 ｜正例： - 把背屏设为… | LOCAL | APP_SIGN |
| `set_back_screen_enabled` | 打开或关闭手机背屏（副屏）总开关。关闭后背屏不再点亮；打开后按系统当前显示策略（智能亮屏 / 常亮 / 定时）工作。仅控制总开关，不调整亮度、常显内容或 Agent 动画状态。 ｜正例： - 打开背屏 - 关闭背屏 - 把副屏关掉 - 开启手机背面的屏幕 ｜反例： - 调背屏亮度 → 不应走本能力 - 把背屏切成时钟 … | LOCAL | APP_SIGN |
| `set_back_screen_frame` | 向背屏推送一帧自定义点阵画面。画布固定为 17 列（x / 宽度）× 23 行（y / 高度），共 391 格。可传 frame 一维整数数组（下标 y * 17 + x，亮度 0–255，0 为灭），或传 text 由本能力把文字（含中文，最多 6 字）栅格化后下发。frame 与 text 二选一。 ｜正例： - … | LOCAL | APP_SIGN |
| `show_notify_by_info` | 根据传入的标题、内容、PendingIntent 和图标生成并显示一条通知。该能力是底层通知展示接口，适用于系统服务、上层应用或后台任务主动展示自定义通知，不适合作为普通用户自然语言直接触发的能力。 ｜正例： - 系统服务根据标题、内容和跳转 intent 展示通知 - 后台任务完成后展示一条自定义通知 - 上层应用传… | LOCAL | APP_SIGN |
| `show_widget_by_package_class` | 根据指定 packageName 和 Widget provider className 展示对应小组件。该能力要求明确传入小组件所属应用包名和完整类名，不负责随机选择小组件。 ｜正例： - 根据指定包名和类名展示小组件 - 展示 com.example.app 的指定 Widget - 按 Widget provid… | LOCAL | APP_SIGN |
| `sleep_back_screen` | 熄灭背屏（sleepBackScreen）。与关闭背屏总开关不同，本能力只请求立刻灭屏，不修改总开关设置。 ｜正例： - 熄灭背屏 - 把副屏关掉亮屏 - 背屏休眠 ｜反例： - 关闭背屏总开关 → 应走 set_back_screen_enabled - 查询背屏亮灭状态 → 应走 get_back_screen_d… | LOCAL | APP_SIGN |
| `start_vibration` | 立即让设备按指定时长进行一次震动，适用于即时触觉提示。重复调用会重新提交震动请求；不创建未来的定时提醒、不循环震动，也不修改系统的来电或通知震动设置。成功返回「已提交震动请求」及采用的时长和强度，不等待震动结束；到期由系统停止，也可调用 stop_vibration 提前取消。返回成功仅表示请求已提交，实际震动仍受硬件… | LOCAL | APP_SIGN |
| `stop_vibration` | 取消当前震动。不关闭系统震动开关，也不禁止后续震动。无需参数，传入的参数会被忽略；成功返回「已提交取消震动请求」，没有正在进行的震动时也正常返回，不查询或报告当前震动状态。权限不足或系统服务异常时返回错误。 ｜正例： - 停止刚才的震动 - 取消你正在发起的震动 ｜反例： - 让手机震动 2 秒 → 应走 start_… | LOCAL | APP_SIGN |
| `wake_up_back_screen` | 点亮背屏（wakeUpBackScreen）。与打开背屏总开关不同，本能力只请求立刻亮屏，不修改总开关设置。 ｜正例： - 点亮背屏 - 把副屏亮起来 - 唤醒背屏 ｜反例： - 打开背屏总开关 → 应走 set_back_screen_enabled - 查询背屏亮灭状态 → 应走 get_back_screen_d… | LOCAL | APP_SIGN |

## 电话

`com.android.dialer`　·　36 项能力　·　手机联系人及通话管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `dialer_accept_call` | 接听当前响铃中的来电。调用 TelecomManager.acceptRingingCall() 后立即返回，不等待通话建立完成；若无来电则行为由系统决定。 ｜正例： - 接听电话 - 帮我接一下这个来电 - 把当前来电接起来 ｜反例： - 挂断当前来电 → 应走 dialer_hangup_call - 拒接这个电话… | LOCAL | APP_SIGN |
| `dialer_add_group` | 在通讯录中创建新的联系人群组。在第一个支持群组的非 SIM 账户下创建，群组名为必填。 ｜正例： - 帮我新建一个联系人群组 - 创建一个家人联系人群组 - 在电话里添加一个联系人分组 ｜反例： - 帮我添加一个联系人 → 应走 dialer_contacts_add | LOCAL | APP_SIGN |
| `dialer_add_number_to_blocked_list` | 号码级操作：将指定号码加入电话黑名单（拦截列表），不删除通话记录。若号码匹配到通讯录联系人，会一并拦截该联系人的所有号码。仅当用户给出具体号码（或明确要拉黑某个号码）时使用。 分工边界：电话 app 负责号码级黑名单加/删/查；打开黑名单/骚扰拦截页面、规则级拦截策略（如拦截陌生来电）应走手机管家的 security_… | LOCAL | APP_SIGN |
| `dialer_call_back` | 回拨通话记录中最近一次通话的号码（按时间倒序取第一条）。找到记录后立即发起语音呼叫并返回，不等待接通；无通话记录时返回提示且不拨号。 ｜正例： - 回拨最近一次通话 - 给刚才通话记录里的号码打回去 - 拨回上一个电话 - 回拨最近联系过的号码 ｜反例： - 拨打指定号码 → 应走 dialer_call_to - 给… | LOCAL | APP_SIGN |
| `dialer_call_contact` | 根据联系人姓名在通讯录中查找并直接拨打电话。仅当用户说的是联系人姓名（非纯数字号码）时使用。参数：name（人名或昵称）、work（可选消歧）、contactId（多候选时指定）。支持昵称匹配（如「妈妈」）；服务端会自动拆分「快递员张三」类复合名。唯一匹配立即拨号；多个匹配返回候选列表，不会自动拨号。 ｜正例： - 给… | LOCAL | APP_SIGN |
| `dialer_call_to` | 给指定电话号码直接拨打电话（立即发起呼叫，不打开拨号盘界面），并可指定是否为视频通话。用户说「给XX打电话」「拨打XX」「打电话给XX」且 XX 为号码（含 10086、110、95xxx 等短号/客服号、手机号、固话）时，必须使用本工具并传入 number=XX。 ｜正例： - 给10086打电话 - 拨打10086… | LOCAL | APP_SIGN |
| `dialer_check_last_caller` | 查询通话记录中最近一次通话的详情（不限于来电，含呼入/呼出/未接等），返回号码、缓存联系人名称、时间和通话类型。仅查询，不拨号。 ｜正例： - 最近一次通话是什么号码 - 刚才那通电话是谁打的 - 帮我看看上一通通话的详情 ｜反例： - 回拨最近一次通话记录里的号码 → 应走 dialer_call_back - 只查… | LOCAL | APP_SIGN |
| `dialer_contacts_add` | 向通讯录新增联系人。号码为必填；姓名、邮箱、公司、职位、备注、地址为可选补充字段，仅写入非空值。 ｜正例： - 帮我添加一个联系人，号码是某某 - 把这个号码存到联系人里，名字叫某某 - 新建一个联系人，保存他的电话和邮箱 - 给某某添加到通讯录，备注一下公司信息 ｜反例： - 修改已有联系人信息 → 应走 diale… | LOCAL | APP_SIGN |
| `dialer_contacts_copy_number` | 将指定联系人的手机号码复制到系统剪贴板。按姓名模糊匹配；唯一匹配时复制并返回，多匹配时返回候选列表，未找到时返回提示。用户仅想查看/查询号码、不要求复制时，应走 dialer_contacts_query。 ｜正例： - 复制张三的手机号 - 把李四的手机号码复制到剪贴板 - 帮我复制一下王五的手机号 ｜反例： - 查… | LOCAL | APP_SIGN |
| `dialer_contacts_delete` | 按条件删除通讯录联系人（Contacts），不打开编辑界面，不修改联系人字段，不是删除通话记录，不是黑名单操作。name/number/address/company 为 string 数组，至少填一个。 硬规则：一次意图只调 1 次本工具；多人/多号全部放进对应数组，禁止拆成多次 tools/call。用户说「删除联… | LOCAL | APP_SIGN |
| `dialer_contacts_query` | 查询通讯录中**当前仍存在**的联系人，支持按姓名/昵称、号码、work 检索（号码优先）。支持昵称（如「妈妈」）；自动拆分「快递员张三」类复合名。返回姓名、电话、work 等。仅用于查看/查询，不删除、不恢复。用户说「撤回/恢复已删联系人」时禁止使用本工具；即使带了姓名、号码或地址要恢复，也禁止先用本工具再 rest… | LOCAL | APP_SIGN |
| `dialer_contacts_restore` | 撤回/恢复 dialer_contacts_delete 删除的联系人（从本地备份写回系统通讯录）。 硬规则：一次意图只调 1 次；多人放进数组，禁止拆多次；带筛选调用后禁止立刻用空参 {} 重试；禁止先 dialer_contacts_query。 筛选 name/number/address/company 可选（… | LOCAL | APP_SIGN |
| `dialer_contacts_set_starred` | 收藏或取消收藏指定联系人。通过号码或姓名定位（至少一个，号码优先）；按姓名匹配到多个时要求提供号码以消歧。 ｜正例： - 把联系人小王设为收藏 - 取消收藏联系人小李 - 把这个号码对应的联系人加到收藏 - 把联系人老张取消星标 ｜反例： - 添加联系人 → 应走 dialer_contacts_add - 复制联系人… | LOCAL | APP_SIGN |
| `dialer_contacts_update` | 修改已有联系人的信息（姓名、邮箱、公司、职位、备注、地址）。通过号码或姓名定位联系人（号码优先，姓名支持模糊匹配）；仅更新传入的非空字段，未传字段保持原值不变。姓名与号码至少提供一个作为定位条件。 副作用边界：不支持修改电话号码，number 仅用于定位；传入非空 name 时同时作为定位条件和新姓名写入；按姓名定位且… | LOCAL | APP_SIGN |
| `dialer_delete_calllog` | 按条件删除系统通话记录（Call Log），不删除通讯录联系人，不操作电话黑名单，不打开任何界面。支持按日期/日期区间/上午下午晚上等时段、联系人姓名、号码过滤，以及删除最近一条；name 与 number 同时提供时为 OR 关系。原 today/yesterday/day_before_yesterday/by_n… | LOCAL | APP_SIGN |
| `dialer_delete_number_from_blocked_list` | 号码级操作：将指定号码从电话黑名单（拦截列表）中移除，不删除系统通话记录，不打开界面。与「删除与某某的通话记录」完全不同。仅当用户给出具体号码并要求取消拉黑时使用。 分工边界：本工具只管单个号码移出黑名单；打开黑名单/骚扰拦截页、关闭骚扰拦截或调整拦截规则应走手机管家的 security_manager_open_ha… | LOCAL | APP_SIGN |
| `dialer_hangup_call` | 挂断当前来电或进行中的通话。通过 TelecomManager.endCall() 执行，成功或失败均立即返回结果。 ｜正例： - 挂断电话 - 帮我挂掉当前通话 - 拒接这个来电 - 把来电挂了 ｜反例： - 接听这个来电 → 应走 dialer_accept_call - 帮我接电话 → 应走 dialer_acc… | LOCAL | APP_SIGN |
| `dialer_open_call_settings` | 打开电话应用设置界面。无需参数，调用后直接跳转。 ｜正例： - 打开电话设置 - 进入通话设置界面 - 帮我打开电话的设置页面 ｜反例： - 开关电源键挂断 → 应走 dialer_settings_enable_power_button_ends_call - 打开 SIM 卡设置 → 应走 dialer_open_… | LOCAL | APP_SIGN |
| `dialer_open_contacts_editor` | 打开指定联系人的编辑界面，不删除联系人、不写入字段。通过号码或姓名定位联系人（至少提供一个）；号码优先。按姓名匹配到多个联系人时返回错误提示，不会打开界面。仅当用户明确要求「打开编辑页」「进入编辑界面」时使用。用户说「删除联系人」「删掉某某」「把某某从通讯录删掉」时禁止使用本工具，应走 dialer_contacts_… | LOCAL | APP_SIGN |
| `dialer_open_medical_emergency_information` | 打开医疗急救信息编辑/查看界面。无需参数。 ｜正例： - 打开医疗急救信息 - 帮我查看医疗急救信息 - 进入医疗急救信息界面 ｜反例： - 开关未解锁查看急救信息 → 应走 dialer_settings_allow_viewing_medical_information - 打开电话设置 → 应走 dialer_o… | LOCAL | APP_SIGN |
| `dialer_open_my_business_card` | 打开「我的名片」界面，展示本地个人档案信息。无需参数，调用后直接跳转。 ｜正例： - 打开我的名片 - 查看我的个人档案 - 把我的本地名片打开 ｜反例： - 查询其他联系人 → 应走 dialer_contacts_query - 编辑其他联系人 → 应走 dialer_open_contacts_editor - … | LOCAL | APP_SIGN |
| `dialer_open_sim_card_settings` | 打开 SIM 卡相关设置界面。无需参数。 ｜正例： - 打开SIM卡设置 - 帮我进入SIM卡设置界面 - 我要设置SIM卡 ｜反例： - 打开电话设置 → 应走 dialer_open_call_settings - 拨打电话 → 应走 dialer_call_to - 查询通话记录 → 应走 dialer_quer… | LOCAL | APP_SIGN |
| `dialer_query_blocked_number` | 号码级操作：查询指定号码是否在电话黑名单（拦截列表）中。仅查询该号码的拦截状态，不查通讯录联系人号码，不打开任何界面。 分工边界：本工具只回答「某个具体号码是否已拉黑」；打开黑名单/骚扰拦截页、查看或调整拦截规则应走手机管家的 security_manager_open_harassment_interception。… | LOCAL | APP_SIGN |
| `dialer_query_call_duration_ranking` | 查询通话时长排行榜，按时长从长到短排序，仅包含时长大于 0 的记录。可选按联系人姓名模糊过滤。 ｜正例： - 查看通话时长排行榜 - 帮我按通话时长排个榜 - 看看我和某个联系人的通话时长排行 ｜反例： - 查通话记录列表 → 应走 dialer_query_calllog - 查未接来电 → 应走 dialer_qu… | LOCAL | APP_SIGN |
| `dialer_query_calllog` | 查询通话记录，支持按日期/日期区间、联系人姓名过滤。未传日期时返回最近记录；按姓名过滤时先查通讯录号码再匹配通话记录。原 today/yesterday/day_before_yesterday/this_morning/this_afternoon/tonight 专用查询已合并到本工具；模型须将自然语言换算为规定日… | LOCAL | APP_SIGN |
| `dialer_query_calllog_by_number` | 按电话号码查询通话记录。对原始号码及去非数字后的号码分别做子串模糊匹配（NUMBER LIKE），与 dialer_delete_calllog（传 number）的精确归一化匹配不同。 ｜正例： - 帮我查一下这个号码的通话记录 - 看看某个联系人号码的通话记录 - 查这个号码最近的通话记录 ｜反例： - 按通讯录里… | LOCAL | APP_SIGN |
| `dialer_query_calllog_by_type` | 按通话类型查询通话记录，如未接、呼入、呼出、语音留言、已拒接、已拦截等。 ｜正例： - 查一下我的未接来电记录 - 帮我看看呼出通话记录 - 查询已拦截的通话记录 - 看看我的语音留言通话记录 ｜反例： - 查指定号码的记录 → 应走 dialer_query_calllog_by_number - 查今天的记录 → … | LOCAL | APP_SIGN |
| `dialer_query_calllog_of_contact` | 按通话记录中显示的联系人名称（缓存姓名 CACHED_NAME）查询相关通话记录，支持姓名模糊匹配；不查询通讯录，不要求对方在通讯录中。与 dialer_query_calllog 的 name 参数不同：后者先查通讯录号码再匹配通话记录。 ｜正例： - 查通话记录里显示为小王的那几条 - 看看通话记录中联系人名称包含… | LOCAL | APP_SIGN |
| `dialer_settings_allow_viewing_medical_information` | 直接开启或关闭「未解锁时允许查看医疗急救信息」设置项，无需打开设置界面。 ｜正例： - 开启未解锁时查看医疗急救信息的开关 - 关闭锁屏时直接查看医疗急救信息 - 把电话设置里的未解锁查看医疗急救信息打开 ｜反例： - 打开急救信息编辑页 → 应走 dialer_open_medical_emergency_infor… | LOCAL | APP_SIGN |
| `dialer_settings_enable_incoming_flip_silent` | 直接开启或关闭「来电翻转静音」设置项，无需打开设置界面。 ｜正例： - 开启来电翻转静音功能 - 关闭来电翻转静音 - 帮我打开翻转静音来电的功能 ｜反例： - 打开电话设置 → 应走 dialer_open_call_settings - 接听来电 → 应走 dialer_accept_call - 接通时振动 → … | LOCAL | APP_SIGN |
| `dialer_settings_enable_power_button_ends_call` | 直接开启或关闭「按电源键挂断电话」设置项，无需打开设置界面。 ｜正例： - 开启按电源键挂断电话功能 - 关闭按电源键挂断电话功能 - 把电源键结束通话打开 - 不要让电源键挂断电话了 ｜反例： - 帮我挂掉现在这通电话 → 应走 dialer_hangup_call - 挂断当前通话 → 应走 dialer_hang… | LOCAL | APP_SIGN |
| `dialer_settings_open_auto_record_screen` | 打开通话自动录音设置界面。无需参数。 ｜正例： - 打开通话录音设置 - 帮我进入电话录音设置界面 - 我要设置通话录音 ｜反例： - 打开电话设置 → 应走 dialer_open_call_settings - 开关电源键挂断 → 应走 dialer_settings_enable_power_button_end… | LOCAL | APP_SIGN |
| `dialer_settings_sos_auto_call` | 直接开启或关闭「SOS 紧急求助时自动报警」设置项，无需打开设置界面。 ｜正例： - 打开SOS紧急求助时的自动报警开关 - 关闭电话设置里的SOS自动报警 - 帮我开启SOS紧急求助自动报警 - 把SOS紧急求助的自动报警关掉 ｜反例： - SOS 求助紧急联系人 → 应走 dialer_settings_sos_a… | LOCAL | APP_SIGN |
| `dialer_settings_vibrate_when_mocall_connected` | 直接开启或关闭「接通时振动」设置项，无需打开设置界面。 ｜正例： - 开启接通电话时振动 - 关闭电话接通时振动提醒 - 把接通时振动功能打开 - 把接通时振动关掉 ｜反例： - 打开电话设置 → 应走 dialer_open_call_settings - 翻转静音 → 应走 dialer_settings_enab… | LOCAL | APP_SIGN |
| `dialer_show_dialpad` | 仅打开拨号盘界面并可选预填号码，不直接发起呼叫。仅当用户明确要求「打开拨号盘」「进入拨号界面」「把号码填到拨号盘」时使用。用户说「给XX打电话」「拨打XX」即使带号码，也应走 dialer_call_to 直接拨号，不要用本工具。 ｜正例： - 打开拨号盘 - 打开拨号盘并输入这个号码 - 帮我把这个号码填到拨号盘里 … | LOCAL | APP_SIGN |
| `dialer_show_incall_screen` | 在已有进行中通话时，拉起系统通话界面（InCall UI）。若当前无通话，返回提示且不打开界面。 ｜正例： - 显示当前通话界面 - 帮我回到通话页面 - 把正在通话的界面拉起来 ｜反例： - 拨打电话 → 应走 dialer_call_to 或 dialer_call_contact - 接听来电 → 应走 dial… | LOCAL | APP_SIGN |

## 信息

`com.android.mms`　·　28 项能力　·　手机短信管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `sms_account_balance_inquiry` | 通过「短信」向运营商发送话费查询指令（移动10086/联通10010/电信10001），异步等待运营商回复。注意：需插入可用 SIM 卡且运营商支持，发送可能产生短信费用。 ｜正例： - 查话费 - 查话费余额 - 我还剩多少话费 - 用卡2查话费 ｜反例： - 查流量余额 → sms_data_balance_inq… | LOCAL | APP_SIGN |
| `sms_data_balance_inquiry` | 通过「短信」向运营商发送流量查询指令（移动/联通/电信均为 CXLL），异步等待运营商回复。注意：需插入可用 SIM 卡且运营商支持，发送可能产生短信费用；不同运营商返回口径可能不同。 ｜正例： - 查流量 - 查剩余流量 - 我还剩多少流量 - 用卡2查流量 ｜反例： - 查话费余额 → sms_account_ba… | LOCAL | APP_SIGN |
| `sms_delete` | 在「短信」中删除短信记录。通过 phone_number（支持联系人名称解析）删除该号码相关的全部短信。注意：破坏性操作，删除后通常不可恢复。 ｜正例： - 删掉和妈妈的所有短信 - 删除13800138000的短信 - 清空和张三的短信记录 ｜反例： - 删除整个对话会话 → sms_thread_delete - … | LOCAL | APP_SIGN |
| `sms_draft_delete` | 在「短信」中删除短信草稿。覆盖新建会话草稿、已有会话草稿（bugle_db）及 telephony 草稿箱。传入 phone_number 删除该号码相关草稿，或设置 delete_all=true 删除全部；同时传入时按 phone_number > delete_all 优先级执行。注意：破坏性操作，删除后通常不可… | LOCAL | APP_SIGN |
| `sms_draft_get` | 在「短信」中查询指定联系人/号码对应会话的草稿。优先读取 bugle_db 会话草稿，其次新建会话草稿（DraftHelper，含收件人号码与显示名），最后兜底查询 telephony 草稿箱。 ｜正例： - 查看给妈妈写的草稿 - 查13800138000的草稿 - 这个联系人的草稿内容是什么 ｜反例： - 保存一条… | LOCAL | APP_SIGN |
| `sms_draft_save` | 在「短信」中保存短信草稿。写入 bugle_db 会话草稿并同步 telephony 草稿箱；已有会话时更新该会话草稿，无会话时创建新草稿。 ｜正例： - 保存草稿 - 先存到草稿箱 - 给妈妈的短信先存草稿 - 把这段内容保存为草稿 ｜反例： - 给张三直接发送短信 → sms_send_direct - 查看给妈妈… | LOCAL | APP_SIGN |
| `sms_forward` | 在「短信」中将已有短信内容直接发送给其他联系人/号码。在 bugle_db 收件箱中按 keywords 模糊匹配短信正文，命中多条取最新一条；未传 keywords 时取最新收到的一条短信。匹配后直接发送，不打开编辑页。 ｜正例： - 把包含验证码的短信转发给妈妈 - 转发给张三看看 - 把取件码短信转发给老王 - … | LOCAL | APP_SIGN |
| `sms_open_collected_list` | 在「短信」中打开已收藏/标星短信列表页面。 ｜正例： - 打开收藏短信 - 查看我收藏的短信 - 进入短信收藏夹 ｜反例： - 打开个人短信列表 → sms_open_personal_list - 打开通知短信 → sms_open_notice_list - 搜索短信内容 → sms_search ｜返回： 成功打… | LOCAL | APP_SIGN |
| `sms_open_notice_list` | 在「短信」中打开通知/服务类短信列表页面，查看验证码、快递、账单等通知短信会话。 ｜正例： - 打开通知短信 - 查看通知类短信 - 只看验证码通知短信 ｜反例： - 打开个人短信列表 → sms_open_personal_list - 打开收藏短信 → sms_open_collected_list - 搜索验证码… | LOCAL | APP_SIGN |
| `sms_open_personal_list` | 在「短信」中打开个人短信列表页面，查看与个人联系人的对话列表（非通知/服务类短信）。 ｜正例： - 打开个人短信 - 进入个人短信列表 - 只看个人聊天短信 ｜反例： - 打开通知短信列表 → sms_open_notice_list - 打开收藏短信 → sms_open_collected_list - 查某个号码… | LOCAL | APP_SIGN |
| `sms_open_settings_page` | 在「短信」中打开短信设置页面，用于配置通知、彩信、回执、拦截等相关选项。 ｜正例： - 打开短信设置 - 进入短信设置页面 - 短信设置在哪 ｜反例： - 打开智慧短信开关 → sms_settings_intelligent_msg - 设置漫游彩信自动下载 → sms_settings_auto_retrieval… | LOCAL | APP_SIGN |
| `sms_read_status` | 在「短信」中设置会话已读/未读状态。传入 phone 时标记该联系人/号码对应会话；不传 phone 且 read=true 时标记全部会话为已读。标记未读与会话列表长按操作语义一致：仅当会话全部已读时生效。 ｜正例： - 把和妈妈的短信都标为已读 - 把这个号码的短信标记成未读 - 清掉所有未读角标 ｜反例： - 删… | LOCAL | APP_SIGN |
| `sms_schedule_send` | 在「短信」中设置短信定时发送，到指定时间自动发送给目标号码。发送时间通过 timestamp、datetime、delay_minutes 三选一指定，时间必须在当前时间之后。 ｜正例： - 明天早上9点给妈妈发短信 - 半小时后自动发送这条短信 - 晚上8点发给张三 - 设置延迟10分钟发送 ｜反例： - 现在就给妈… | LOCAL | APP_SIGN |
| `sms_search` | 在「短信」中按正文关键词、联系人名称/号码、日期/时间范围、收发类型组合搜索或查询短信，至少提供一个搜索条件，结果按时间倒序返回。 关键参数区分：查「某人/某号码」的短信（如「查一下弟弟的短信」「看看和妈妈的短信」）必须传 phone，禁止把联系人名称或手机号放进 keyword；keyword 仅用于匹配短信正文内容… | LOCAL | APP_SIGN |
| `sms_send` | 在「短信」中发送短信或保存草稿。收件人支持联系人名称或手机号；send_directly=true 时直接后台发送，false 时写入草稿箱并打开编辑页。超长短信自动拆分，可选指定 SIM 卡槽。 ｜正例： - 给妈妈发短信说我晚点到 - 发条短信给张三 - 给13800138000发我到家了 - 先存成草稿别发 - … | LOCAL | APP_SIGN |
| `sms_send_direct` | 在「短信」中给指定联系人或手机号直接发送短信，不保存草稿、不打开编辑页。收件人支持联系人名称或手机号，超长短信自动拆分。 ｜正例： - 马上给老王发短信说到了 - 给13800138000发到楼下了 - 发消息给妈妈说我晚点到 - 直接发出去别存草稿 ｜反例： - 把这条短信先存成草稿 → sms_send - 保存一… | LOCAL | APP_SIGN |
| `sms_settings_auto_retrieval` | 在「短信-设置」中设置「漫游时彩信自动下载（MMS）」开关。双卡时可指定 SIM1/SIM2，未指定时两张卡同时设置。注意：开启后漫游环境可能产生数据流量费用。 ｜正例： - 漫游时别自动下彩信 - 打开漫游彩信自动下载 - 关闭SIM1漫游自动下载彩信 ｜反例： - 打开短信设置页面 → sms_open_setti… | LOCAL | APP_SIGN |
| `sms_settings_center_num` | 在「短信-设置」中设置短信中心号码（SMSC），支持为指定 SIM 卡配置。注意：配置错误可能导致短信发送失败，请按运营商提供的信息填写。 ｜正例： - 设置短信中心号码 - 修改SMSC - 把SIM1短信中心号改成+8613800138000 ｜反例： - 查看SIM卡短信 → sms_settings_sim_m… | LOCAL | APP_SIGN |
| `sms_settings_delivery_reports` | 在「短信-设置」中开启或关闭「短信送达报告/送达回执」开关。双卡时可指定 SIM1/SIM2，未指定时两张卡同时设置。注意：送达回执受运营商与对方网络支持影响，可能无法返回。 ｜正例： - 打开短信送达回执 - 关闭送达报告 - 发短信要显示送达状态 ｜反例： - 漫游彩信自动下载设置 → sms_settings_a… | LOCAL | APP_SIGN |
| `sms_settings_expired_pickup` | 在「短信-设置」中开启或关闭「自动删除取件码短信」开关，控制取件码类短信过期后是否自动清理。注意：为破坏性操作，开启后过期取件码将被自动删除。 ｜正例： - 取件码短信自动删除 - 打开取件码自动清理 - 关闭自动删取件码短信 ｜反例： - 自动删除验证码短信 → sms_settings_expired_veri -… | LOCAL | APP_SIGN |
| `sms_settings_expired_veri` | 在「短信-设置」中开启或关闭「自动删除验证码短信」开关，控制验证码类短信过期后是否自动清理。注意：为破坏性操作，开启后过期验证码将被自动删除。 ｜正例： - 验证码短信自动删除 - 打开验证码自动清理 - 关闭自动删验证码短信 ｜反例： - 自动删除取件码短信 → sms_settings_expired_pickup… | LOCAL | APP_SIGN |
| `sms_settings_intelligent_msg` | 在「短信-设置」中开启或关闭「智慧短信」功能开关。 ｜正例： - 打开智慧短信 - 关闭智慧短信 - 开启智能短信识别 ｜反例： - 打开短信设置页面 → sms_open_settings_page - 打开通知短信列表 → sms_open_notice_list ｜返回： 成功返回「设置智慧短信开关成功」；ena… | LOCAL | APP_SIGN |
| `sms_settings_notif_detail` | 在「短信-设置」中设置通知是否显示短信内容详情。开启后通知/锁屏显示正文，关闭后仅显示提示。 ｜正例： - 通知里显示短信内容 - 锁屏别显示短信详情 - 打开短信通知预览 ｜反例： - 打开短信设置页面 → sms_open_settings_page - 打开漫游彩信自动下载 → sms_settings_auto… | LOCAL | APP_SIGN |
| `sms_settings_quick_reply` | 在「短信-设置」中编辑「快速回复」内容，按序号更新指定条目的文本。 ｜正例： - 把第1条快速回复改成马上到 - 修改短信快捷回复 - 更新快速回复内容 ｜反例： - 给指定号码发短信 → sms_send_direct - 打开短信设置页面 → sms_open_settings_page ｜返回： 成功返回「编辑快… | LOCAL | APP_SIGN |
| `sms_settings_risk_url` | 在「短信-设置」中开启或关闭「风险网址识别/拦截提示」开关，用于识别短信中的可疑链接并提示风险。 ｜正例： - 打开短信风险链接识别 - 关闭风险网址提示 - 开启短信链接防诈骗 ｜反例： - 打开短信设置页面 → sms_open_settings_page - 自动删除验证码短信 → sms_settings_ex… | LOCAL | APP_SIGN |
| `sms_settings_sim_messages` | 在「短信-设置」中读取 SIM 卡内置短信列表（SIM 短信），按时间倒序返回。 ｜正例： - 查看SIM卡短信 - 看看SIM1里存的短信 - 读取SIM短信列表 ｜反例： - 查这个号码的短信 → sms_search - 设置短信中心号码 → sms_settings_center_num ｜返回： 返回 SIM… | LOCAL | APP_SIGN |
| `sms_statistics` | 在「短信」中获取短信数量统计，包括总计、收件箱、已发送、草稿箱、待发送、发送失败、未读数量及会话数。 ｜正例： - 短信有多少条 - 我有多少未读短信 - 草稿箱有几条 - 短信概览统计 ｜反例： - 搜索包含验证码的短信 → sms_search - 查今天收到的短信 → sms_search - 查某个号码的短信 … | LOCAL | APP_SIGN |
| `sms_thread_delete` | 在「短信」中删除短信会话（含该会话内全部短信及 MMS）。phone_number、contact_name 二选一，或设置 delete_all=true 删除全部会话；同时传入多个时按 delete_all > phone_number > contact_name 优先级执行。注意：破坏性操作，删除后通常不可恢复… | LOCAL | APP_SIGN |

## 文件管理

`com.stepos.filemanager`　·　26 项能力　·　手机文件查询及管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `filemanager_create_file` | 在文件管理中创建指定名称的文件；可指定目标文件夹路径，未指定时在内部存储根目录下创建。 ｜正例： - 帮我在 /storage/emulated/0/Download 下创建一个新文件 - 在工作文件夹里新建一个会议记录文件 - 帮我创建一个指定名称的文件 - 在根目录新建一个笔记.txt 文件 ｜反例： - 帮我创建… | LOCAL | APP_SIGN |
| `filemanager_create_folder` | 在文件管理中创建指定名称的文件夹。 ｜正例： - 帮我新建一个文件夹，名字叫工作资料 - 创建一个名为照片备份的文件夹 - 在文件管理里新建一个文件夹 ｜反例： - 帮我新建一个文件 → 应走 filemanager_create_file | LOCAL | APP_SIGN |
| `filemanager_edit_file_name` | 修改指定文件的名称。 ｜正例： - 把这个文件改个名字 - 将这份文件重命名为新的文件名 - 帮我修改这个文件的名称 | LOCAL | APP_SIGN |
| `filemanager_edit_folder_name` | 修改指定文件夹的名称。 ｜正例： - 把这个文件夹改名为工作资料 - 帮我重命名这个文件夹 - 把这个文件夹名称改一下 | LOCAL | APP_SIGN |
| `filemanager_get_apk_file_list` | 获取文件管理中的 APK 文件列表。 ｜正例： - 帮我列出手机里的 APK 文件 - 查看有哪些安装包文件 - 获取 APK 文件列表 ｜反例： - 搜索名称里包含 APK 的文件 → 应走 filemanager_search_file - 查看某个 APK 文件的详细信息 → 应走 filemanager_get… | LOCAL | APP_SIGN |
| `filemanager_get_bluetooth_file_list` | 获取通过蓝牙传输的文件列表。 ｜正例： - 查看蓝牙传输的文件列表 - 帮我找一下蓝牙传过来的文件 - 列出蓝牙接收的文件 ｜返回： 返回 JSON 数组，每项包含 path 和 mIsDir；范围为 /storage/emulated/0/Download/Bluetooth 目录（蓝牙接收目录），包含文件和文件夹；… | LOCAL | APP_SIGN |
| `filemanager_get_browser_file_list` | 获取浏览器内的文件列表。 ｜正例： - 帮我看看浏览器里有哪些文件 - 获取浏览器内的文件列表 - 列出浏览器里的文件 ｜返回： 返回 JSON 数组，每项包含 path 和 mIsDir；范围为 /storage/emulated/0/Download/Browser 目录（浏览器下载目录），不递归子目录；无结果时返… | LOCAL | APP_SIGN |
| `filemanager_get_compress_file_list` | 获取文件管理中的压缩类文件列表。 ｜正例： - 查看压缩类文件列表 - 帮我列出手机里的压缩类文件 ｜返回： 返回 JSON 数组，每项包含 path 和 mIsDir；扫描范围为文件管理压缩包分类（如 zip、rar、7z 等），按分类默认排序；无结果时返回「暂无搜索到匹配内容」。 | LOCAL | APP_SIGN |
| `filemanager_get_document_file_list` | 获取文件管理中的文档类文件列表。 ｜正例： - 查看我的文档文件列表 - 帮我列出文档类文件 - 获取手机里的文档列表 ｜反例： - 搜索某个文件或文件夹 → 应走 filemanager_search_file - 查看某个文件的详细信息 → 应走 filemanager_get_file_detail ｜返回： 返… | LOCAL | APP_SIGN |
| `filemanager_get_download_file_list` | 获取文件管理中的下载文件列表。 ｜正例： - 帮我查看下载文件列表 - 打开文件管理里的下载列表 - 列出我下载过的文件 ｜反例： - 帮我搜索下载的文件 → 应走 filemanager_search_file - 查看某个下载文件的详细信息 → 应走 filemanager_get_file_detail - 获取… | LOCAL | APP_SIGN |
| `filemanager_get_file_create_time` | 获取指定文件的创建时间。 ｜正例： - 查一下这个文件的创建时间 - 获取这个文件是什么时候创建的 - 帮我看看这个文件的创建日期 ｜反例： - 查一下这个文件最后什么时候更新的 → 应走 filemanager_get_file_update_time - 查看这个文件的详细信息 → 应走 filemanager_g… | LOCAL | APP_SIGN |
| `filemanager_get_file_detail` | 获取指定文件的详细信息。 ｜正例： - 查看这个文件的详细信息 - 获取这个文件的详情 - 帮我看一下这个文件的信息 ｜反例： - 获取这个文件的绝对路径 → 应走 filemanager_get_file_path - 查看这个文件的大小 → 应走 filemanager_get_file_size - 查看这个文件… | LOCAL | APP_SIGN |
| `filemanager_get_file_path` | 获取指定文件的绝对路径。 ｜正例： - 获取这个文件的绝对路径 - 帮我查一下这个文件的完整路径 ｜反例： - 查看这个文件的详细信息 → 应走 filemanager_get_file_detail ｜返回： 返回文件的本地绝对路径字符串；无法解析时返回错误信息。 | LOCAL | APP_SIGN |
| `filemanager_get_file_size` | 获取指定文件的大小。 ｜正例： - 查看这个文件有多大 - 帮我获取这个文件的大小 - 这个文件占多少空间 ｜反例： - 查看这个文件的详细信息 → 应走 filemanager_get_file_detail - 获取这个文件的绝对路径 → 应走 filemanager_get_file_path - 查看这个文件的… | LOCAL | APP_SIGN |
| `filemanager_get_file_update_time` | 获取指定文件的最后更新时间。 ｜正例： - 帮我查一下这个文件的最后更新时间 - 这个文件最后什么时候更新的 - 获取这个文件的更新时间 ｜反例： - 查一下这个文件的创建时间 → 应走 filemanager_get_file_create_time - 获取这个文件的大小 → 应走 filemanager_get_… | LOCAL | APP_SIGN |
| `filemanager_get_garbage_file_list` | 获取文件管理中回收站的文件列表。 # workflow 恢复回收站文件时，必须先调用本接口获取列表，再使用返回项中的 garbagePath 调用 filemanager_recovery_garbage_file 或 filemanager_recovery_garbage_files；不可使用 originalPa… | LOCAL | APP_SIGN |
| `filemanager_get_ringtone_file_list` | 获取文件管理中的铃声类文件列表。 ｜正例： - 帮我列出铃声文件 - 获取手机里的铃声类文件列表 - 查看有哪些铃声文件 ｜反例： - 获取某个铃声文件的详细信息 → 应走 filemanager_get_file_detail - 获取某个铃声文件的绝对路径 → 应走 filemanager_get_file_pat… | LOCAL | APP_SIGN |
| `filemanager_get_screen_recording_file_list` | 获取文件管理中的录屏文件列表。 ｜正例： - 查看我的录屏文件 - 把录屏文件列表给我 - 文件管理里有哪些录屏 ｜反例： - 查看某个录屏文件的详细信息 → 应走 filemanager_get_file_detail - 获取某个录屏文件的大小 → 应走 filemanager_get_file_size - 搜索… | LOCAL | APP_SIGN |
| `filemanager_get_screenshot_file_list` | 获取文件管理中的截屏文件列表。 ｜正例： - 帮我列出截屏文件 - 查看我的截屏文件列表 - 获取截屏文件列表 ｜反例： - 获取某个截屏文件的绝对路径 → 应走 filemanager_get_file_path - 查看某个截屏文件的详细信息 → 应走 filemanager_get_file_detail - 搜… | LOCAL | APP_SIGN |
| `filemanager_get_video_file_list` | 获取视频类文件列表。 ｜正例： - 帮我获取视频类文件列表 - 查看视频文件列表 - 看一下手机里所有的视频文件 ｜反例： - 搜索一下视频文件 → 应走 filemanager_search_file ｜返回： 返回 JSON 数组，每项包含 path 和 mIsDir；不传 file_uri 或传入内部存储根路径时… | LOCAL | APP_SIGN |
| `filemanager_get_voice_file_list` | 获取文件管理中的音频类文件列表。 ｜正例： - 查看我的音频文件列表 - 把文件管理里的音频文件列出来 - 有哪些音频文件 ｜反例： - 搜索名叫某某的音频文件 → 应走 filemanager_search_file - 查看某个音频文件的详细信息 → 应走 filemanager_get_file_detail ｜… | LOCAL | APP_SIGN |
| `filemanager_get_weixin_file_list` | 获取微信内的文件列表。 ｜正例： - 帮我查看微信里的文件列表 - 获取一下微信内的文件 - 列出微信里的文件 ｜反例： - 帮我搜索文件管理里的文件 → 应走 filemanager_search_file - 查看某个文件的详细信息 → 应走 filemanager_get_file_detail ｜返回： 返回 … | LOCAL | APP_SIGN |
| `filemanager_move_file` | 将指定源真实路径的文件移动到目标真实路径。 ｜正例： - 把这个文件移动到目标文件夹 - 将源路径里的文件移到目标路径 - 帮我把文件挪到另一个位置 | LOCAL | APP_SIGN |
| `filemanager_recovery_garbage_file` | 根据回收站文件真实路径恢复回收站中的单个文件。 # workflow 必须先调用 filemanager_get_garbage_file_list 获取 garbagePath，再传入本接口；批量或全部恢复请使用 filemanager_recovery_garbage_files。 ｜正例： - 把回收站里的这个文… | LOCAL | APP_SIGN |
| `filemanager_recovery_garbage_files` | 批量恢复文件管理回收站中的文件，支持按 garbagePath 列表、originalPath 前缀或全部恢复。 # workflow 1. 先调用 filemanager_get_garbage_file_list 获取回收站列表。 2. 全部恢复：restoreAll=true。 3. 恢复指定目录（如 Downl… | LOCAL | APP_SIGN |
| `filemanager_search_file` | 在文件管理中根据关键词搜索或查询文件、文件夹。 ｜正例： - 帮我搜索一下文件名里有合同的文件 - 查找名字里有照片的文件夹 - 在文件管理里搜一下包含报告的文件 ｜反例： - 查一下手机里的 apk 文件列表 → 应走 filemanager_get_apk_file_list ｜返回： 返回 JSON 数组，每项包… | LOCAL | APP_SIGN |

## 百度网盘

云端服务　·　18 项能力　·　接入百度网盘MCP

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `baidu-netdisk-mcp_auth_card` | 获取百度网盘（baidu-netdisk-mcp）的授权引导卡片。用户首次使用百度网盘、需要绑定百度网盘账号或完成第三方账号授权时调用。 | CLOUD | - |
| `baidu-netdisk-mcp_auth_revoke` | 取消百度网盘（baidu-netdisk-mcp）的第三方账号授权。用户要求解除百度网盘账号绑定或取消百度网盘授权时调用。 | CLOUD | - |
| `baidu_netdisk_file_copy` | 复制用户百度网盘中的指定文件到网盘目标目录。适用于复制百度网盘文件、在网盘内保留文件副本。 | CLOUD | - |
| `baidu_netdisk_file_doc_list` | 获取用户百度网盘中指定目录下的文档列表。适用于查看百度网盘里有哪些文档；不用于读取或总结文档正文。 | CLOUD | - |
| `baidu_netdisk_file_image_list` | 获取用户百度网盘中指定目录下的图片列表。适用于查看百度网盘中的图片、照片文件。 | CLOUD | - |
| `baidu_netdisk_file_keyword_search` | 按文件名关键词搜索用户百度网盘中的文件，返回指定目录下文件名包含关键词的文件列表。适用于按名称查找百度网盘文件。 | CLOUD | - |
| `baidu_netdisk_file_list` | 获取用户百度网盘中指定目录下的文件列表，不限定文件类型。适用于查看百度网盘文件、浏览网盘目录。 | CLOUD | - |
| `baidu_netdisk_file_meta` | 通过文件ID获取用户百度网盘中文件的详细信息。适用于查看百度网盘文件的元信息；不用于读取文件正文。 | CLOUD | - |
| `baidu_netdisk_file_move` | 移动用户百度网盘中的指定文件到网盘目标目录。适用于移动百度网盘文件、整理网盘目录。 | CLOUD | - |
| `baidu_netdisk_file_rename` | 重命名用户百度网盘中的指定文件。适用于修改百度网盘文件名。 | CLOUD | - |
| `baidu_netdisk_file_semantics_search` | 搜索用户百度网盘中的文件，支持自然语言描述的复杂查询。适用于记不清文件名、按内容线索或语义查找百度网盘文件；不用于读取或总结文件全文。 | CLOUD | - |
| `baidu_netdisk_file_sharelink_set` | 为用户百度网盘中的指定文件创建分享链接。适用于分享百度网盘文件、生成网盘分享链接。 | CLOUD | - |
| `baidu_netdisk_file_upload_by_content` | 将文本内容保存为文件并上传到用户百度网盘。适用于把笔记、文章或生成的文本内容存入百度网盘。 | CLOUD | - |
| `baidu_netdisk_file_upload_by_url` | 通过文件的可下载URL链接上传文件到用户百度网盘。适用于把链接指向的文件保存到百度网盘。 | CLOUD | - |
| `baidu_netdisk_file_video_list` | 获取用户百度网盘中指定目录下的视频列表。适用于查看百度网盘里有哪些视频文件；不用于播放或解析视频内容。 | CLOUD | - |
| `baidu_netdisk_get_quota` | 获取用户百度网盘的空间使用情况。适用于查询百度网盘总容量、已用空间和剩余空间。 | CLOUD | - |
| `baidu_netdisk_make_dir` | 在用户百度网盘中创建文件夹。适用于新建百度网盘目录、创建网盘文件夹。 | CLOUD | - |
| `baidu_netdisk_user_info` | 获取用户百度网盘账号的基本信息。适用于查询已授权的百度网盘账号信息。 | CLOUD | - |

## 手机管家

`com.stepos.safe`　·　12 项能力　·　手机管家，提供骚扰拦截，空间清理，病毒查杀等能力

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `security_center_acceleration_execute` | 立即执行内存清理/手机清理，扫描并清理可杀后台应用以释放内存，无需打开页面或点击桌面快捷方式。短时间内重复调用会直接返回已优化结果，不会报错。用户说法示例：帮我清理后台、一键加速、清一下内存、手机卡了清理后台应用、释放一下运行内存、把后台应用都关掉、帮我加速一下手机。 | LOCAL | APP_SIGN |
| `security_center_acceleration_shortcut_enable` | 在安全中心中为「一键加速」在桌面创建或移除快捷方式，参数 enable 为开则创建、为关则删除，无需进入多层设置页即可完成。用户说法示例：桌面加一键加速、删掉加速图标、我想点一下桌面就清内存、把一键清理放桌面、不要加速快捷方式了、帮我弄个清理加速的快捷方式。 | LOCAL | APP_SIGN |
| `security_center_enable_function` | 在安全中心中一键开启或关闭手机管家核心功能总开关，会影响骚扰拦截、病毒查杀等多项防护是否生效；参数 enable 为开则恢复全套能力、为关则整体关闭。用户说法示例：把手机管家全打开、关掉整个手机管家、先别用管家了我玩游戏、恢复管家全部功能、管家总开关在哪、开启完整安全防护。注意：关闭后多项安全能力可能停用，建议二次确认… | LOCAL | APP_SIGN |
| `security_center_into_practicaltools_page` | 在安全中心内进入「实用工具」页面，可集中管理一键加速、安全扫码、一键锁屏等桌面快捷方式相关能力。用户说法示例：打开实用工具、进管家工具页、我想设桌面加速快捷方式、安全中心工具在哪、到手机管家工具那一页、帮我进实用工具设置。 | LOCAL | APP_SIGN |
| `security_center_lock_screen_shortcut_enable` | 创建或删除手机管家的一键锁屏快捷方式。 ｜正例： - 帮我创建一键锁屏快捷方式 - 把一键锁屏快捷方式删掉 | LOCAL | APP_SIGN |
| `security_center_network_pay_enable` | 开启或关闭手机管家的移动网络安全支付功能。 ｜正例： - 开启移动网络安全支付 - 把移动网络安全支付关掉 - 帮我打开移动网络安全支付功能 ｜反例： - 开启金融支付保护 → 应走 security_center_pay_enable - 关闭金融支付保护 → 应走 security_center_pay_enabl… | LOCAL | APP_SIGN |
| `security_center_open_main` | 打开手机管家应用 ｜正例： - 打开手机管家 - 进入手机管家 - 帮我打开手机管家应用 ｜反例： - 打开手机管家的实用工具页面 → 应走 security_center_into_practicaltools_page - 打开手机管家的骚扰拦截 → 应走 security_manager_open_harassm… | LOCAL | APP_SIGN |
| `security_center_pay_enable` | 开启或关闭手机管家的金融支付保护功能。 ｜正例： - 帮我开启金融支付保护 - 把金融支付保护关掉 - 打开手机管家的支付保护 ｜反例： - 开启移动网络安全支付保护 → 应走 security_center_network_pay_enable | LOCAL | APP_SIGN |
| `security_center_safe_scan_shortcut_enable` | 创建或删除手机管家的安全扫码快捷方式。 ｜正例： - 创建安全扫码快捷方式 - 删除安全扫码快捷方式 | LOCAL | APP_SIGN |
| `security_center_usb_install_enable` | 在安全中心中开启或关闭 USB 安装管理，用于限制或允许通过数据线、电脑侧向本机安装应用；参数 enable 为开则启用管控、为关则放宽对应限制（以系统与管家实际策略为准）。用户说法示例：打开 USB 安装管理、用电脑给我装个应用别拦、插上数据线不让随便装软件、关掉 USB 装应用限制、电脑助手安装被挡了、允许 USB… | LOCAL | APP_SIGN |
| `security_manager_into_virus_page` | 打开病毒查杀 ｜正例： - 打开病毒查杀 - 帮我进入病毒查杀页面 - 我要查杀手机病毒 | LOCAL | APP_SIGN |
| `security_manager_open_harassment_interception` | 打开手机管家的骚扰拦截页面。 ｜正例： - 打开骚扰拦截 - 帮我进入骚扰拦截 - 打开手机管家的骚扰拦截页面 | LOCAL | APP_SIGN |

## 曹操出行

云端服务　·　12 项能力　·　曹操出行

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `caocao-mcp_auth_card` | 检查曹操出行授权及免密支付/智能叫车开通状态，按结果返回授权卡、开通卡或已授权状态 | CLOUD | - |
| `caocao-mcp_auth_revoke` | 取消/撤销曹操出行授权。调用后，用户需重新进行曹操授权操作。 | CLOUD | - |
| `trip_call_driver` | 当用户需要电话联系司机时，获取本单司机的虚拟联系号码。前提是该订单已指派司机；返回的号码为本单专属虚拟号，请原样转述给用户。 | CLOUD | - |
| `trip_cancel_order_v2` | 取消打车订单，取消时必须让用户二次确认一下，用户二次确认后userConfirm传入true才能成功取消。 | CLOUD | - |
| `trip_contact_customer_service` | 当用户表达投诉、报障、找人工等诉求时，获取客服联系方式。仅返回客服渠道信息，不要代替客服承诺任何处理结果。 | CLOUD | - |
| `trip_create_invoice` | 当用户要求开发票时，为该订单提交开票申请。需先确认发票类型：个人开票只需邮箱，公司开票还需填写抬头与税号；提交后发票由邮件发送，不在会话内返回发票文件。 | CLOUD | - |
| `trip_create_order_v2` | 使用曹操登录后估价产生的有效 estimateId 及所选车型编码创建订单并开始匹配司机。成功执行会产生真实订单；请求超时时执行结果可能未知 | CLOUD | - |
| `trip_estimate_v2` | 按起终点地址查询曹操出行可用车型和预估价格，支持直接解析地址。返回 estimateId、匹配地点、车型和价格信息；tripScene 为出行场景参数 | CLOUD | - |
| `trip_query_history_orders` | 根据时间、地点、价格查询历史订单信息，包含是否开过发票。时间跨度不能超过30天 | CLOUD | - |
| `trip_query_order_v2` | 查询进行中的打车订单信息，例如车牌号、司机联系方式、司机接驾距离、预估到达时间等等。没有orderNoList时，自动查询用户全部行程中订单。 | CLOUD | - |
| `trip_rate_driver` | 行程结束后，为本单司机提交评分与评价。需要用户明确给出评分意愿后再调用，不要主动替用户打分。 | CLOUD | - |
| `trip_send_driver_message` | 给司机留言，给司机发消息 | CLOUD | - |

## 日历

`com.android.calendar`　·　11 项能力　·　日程查看及管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `calendar_add_event` | 在用户日历中新增一个日程事件，支持设置标题、描述、地点、起止时间、全天事件、提醒提前时长、以及重复规则（每天/每个工作日/每周/每月/每年/每两周）。 ｜正例： - 帮我在日历里加一个明天下午和客户沟通的日程 - 周五全天团建，帮我加到日历里 - 每周一上午开例会，帮我新增一个重复日程 - 明天上午在会议室开项目会，提… | LOCAL | APP_SIGN |
| `calendar_add_special_event` | 在用户日历中新增生日、纪念日、倒数日等特殊事件。 ｜正例： - 帮我在日历里添加一个生日提醒 - 把我们的纪念日加到日历里 - 在日历里新增一个倒数日事件 ｜反例： - 打开添加特殊事件的页面 → 应走 calendar_open_new_edit_event_activity - 帮我在日历里新增一个普通日程 → 应… | LOCAL | APP_SIGN |
| `calendar_delete_event` | 删除用户日历中的普通日程事件。按 start_time/end_time 圈定要查找的时间区间，再结合可选的 title/description/location 精确定位，唯一匹配一条时执行删除。重复日程与新建写入的是同一行 Events，匹配到后按整条系列删除。 ｜正例： - 删除明天上午的会议日程 - 把我在公司… | LOCAL | APP_SIGN |
| `calendar_delete_special_event` | 在用户日历中按时间范围删除特殊事件（生日、纪念日、倒数日）。通过 start_time/end_time 圈定要删除的时间区间；通过 event_types 指定要删除的特殊事件类型，不传或为空时默认删除该范围内全部三类特殊事件。不会影响普通日程。 ｜正例： - 删除今天的生日 - 把最近几天的纪念日删掉 - 删除这个… | LOCAL | APP_SIGN |
| `calendar_edit_event` | 在用户日历中编辑一个日程事件，一次仅修改该事件的时间或标题之一。start_time/end_time 用于圈定要查找目标日程的时间区间，配合可选 title 精确定位。 ｜正例： - 把明天上午的会议改到下午 - 帮我把今晚的日程标题改一下 - 把下周一的日程改个时间 - 把今天的会议标题改成团队复盘 ｜反例： - … | LOCAL | APP_SIGN |
| `calendar_edit_special_event` | 编辑用户日历中的特殊事件，支持修改生日、纪念日或倒数日的时间、标题或提醒设置。 ｜正例： - 把日历里的生日提醒改成提前一天提醒 - 帮我修改一个纪念日的标题 - 把倒数日的日期改一下 - 把这个特殊事件的提醒时间改一下 ｜反例： - 把普通日程的标题改一下 → 应走 calendar_edit_event - 只传 … | LOCAL | APP_SIGN |
| `calendar_open_almanac_detail_activity` | 打开/进入黄历详情页面。可查看当天黄历的宜忌、吉凶、冲煞等内容。 示例话术：打开黄历；我想看看今天的黄历；查看今天的宜忌和冲煞；进入日历里的黄历页面。 | LOCAL | APP_SIGN |
| `calendar_open_general_settings` | 打开/进入日历设置页面。该页面包含通用设置（通知和提醒、每周起始日、默认日历视图）、智能识别日程开关、页面显示开关（农历详情卡片/显示周数/显示节日/显示过去的事件/显示拒绝事件/日程分享水印）以及个性化等相关设置。仅打开页面，不修改任何设置项。 示例话术：打开日历设置；进入通用设置页面；我想设置通知和提醒；打开显示节… | LOCAL | APP_SIGN |
| `calendar_open_new_edit_event_activity` | 打开/进入新建日程页面（仅打开，不直接创建内容）。该页面支持创建普通日程事件，以及创建特殊事件（生日/纪念日/倒数日），由用户自行填写并保存。 示例话术：打开日历的添加日程页面；进入新建日程界面；我想创建生日或纪念日，先打开添加页面；打开添加倒数日的页面。 不要用于：直接在日历里新增普通日程（请改用 calendar_… | LOCAL | APP_SIGN |
| `calendar_query_event` | 在用户日历中根据开始时间和结束时间查询日程。 ｜正例： - 查一下今天的日程 - 看看我明天有哪些日程 - 帮我查最近几天的日历安排 - 查询一下这周的日程 ｜返回： 成功时返回文本：「查询到N条日程数据：」+ JSON 数组（ScheduleMcpEvent）。字段：title、description、locatio… | LOCAL | APP_SIGN |
| `calendar_query_special_event` | 在用户日历中根据开始时间和结束时间查询特殊事件（生日/纪念日/倒数日）。event_types 指定查询类型，不传或为空时查询全部类型。 ｜正例： - 查一下今天的特殊事件 - 帮我找本周的生日 - 看看这个月有哪些纪念日 - 查询最近几天的倒数日 ｜反例： - 查询今天有哪些日程 → 应走 calendar_quer… | LOCAL | APP_SIGN |

## 网络设置

`com.stepos.connectivitysettings`　·　11 项能力

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `connectivitysettings_open_settings_advanced_wifi_settings_activity` | 打开/进入 WiFi 高级设置页面。此页面包括公共网络提醒、证书安装、MAC地址切换等功能。 ｜正例： - 打开 WiFi 高级设置 - 进入 WiFi 高级设置 - 打开 WiFi 高级设置页面 - 进入 WiFi 高级设置页面 - 查看 WiFi 高级设置 ｜反例： - 打开 WiFi 设置页面 → 应走 conn… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_bluetooth_settings_activity` | 打开系统设置中的蓝牙页面，用于配对/管理蓝牙设备（非开关）。 ｜正例： - 打开蓝牙设置 - 蓝牙配对 - 连蓝牙设备 - 管理蓝牙 - 查看蓝牙设备 - 查看蓝牙设备列表 ｜反例： - 打开蓝牙开关 → 不走页面跳转 | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_mobile_network_settings_activity` | 打开/进入 SIM 卡管理页面，并进入双卡管理页面。此界面包含双卡数据切换和流量开关控制等功能。 ｜正例： - 打开SIM卡管理页面 - 进入双卡管理页面 - 查看双卡管理页面 - 查看SIM卡管理 - 查看流量设置 - 打开数据网络页面 ｜反例： - 打开网络设置 → 应走 connectivitysettings_… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_nfc_settings_activity` | 打开 NFC 设置页面。此功能不会直接打开 NFC 开关，而是显示 NFC 设置页面，您可以在其中配置 NFC 功能。 ｜正例： - 打开NFC设置 - 进入NFC设置页面 - 查看NFC设置 - 打开卡包设置 - 查看卡包设置 ｜反例： - 打开NFC开关 → 不走页面跳转 | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_saved_access_points_wifi_settings` | 打开/进入已保存WiFi页面。该页面是管理WiFi的展示页面，可以选择某一个已保存的WIFI，进行取消保存、断开连接、分享、查看该WIFI的详情信息等操作。 ｜正例： - 打开已保存的WiFi页面 - 进入已保存WiFi列表 - 查看我保存过的WiFi - 管理已保存的WiFi - 查看有哪些已保存的WiFi ｜反例：… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_tether_settings_activity` | 打开设置中的热点页面或网络共享页面，供用户进入热点与网络共享相关设置。 ｜正例： - 打开个人热点设置 - 进入网络共享页面 - 打开热点和网络共享设置 - 我想设置手机热点 - 查看热点和网络共享设置 - 进入热点和网络共享设置 ｜反例： - 打开 WiFi 设置 → 应走 connectivitysettings_… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_vpn_settings_activity` | 打开/进入VPN连接页面。该页面可以对VPN进行添加/配置，设置VPN相关偏好。 ｜正例： - 打开VPN连接页面 - 进入VPN设置 - 我要配置VPN - 帮我打开VPN偏好设置 - 查看VPN设置 - 添加VPN配置 ｜反例： -打开VPN开关 → 不走页面跳转 | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_wifi_display_settings_activity` | 打开/进入投屏的设置界面，该功能不直接打开投屏的开关，而是展示投屏页面，进入之后可以搜索附近可投屏的设备，从而进行后续的连接操作。 ｜正例： - 打开投屏设置 - 进入无线投屏页面 - 打开投屏页面搜索附近设备 - 我想连接附近可投屏的设备 - 查看附近可投屏的设备 ｜反例： - 打开 WiFi 设置页面 → 应走 c… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_wifi_info_settings_activity` | 打开当前连接的 WiFi 详情页面，用于查看当前连接WiFi信息并进入该 Wi-Fi 的相关设置。 ｜正例： - 打开当前连接的 WiFi 详情 - 看看我现在连的 WiFi 详细信息 - 进入当前 WiFi 的详情页面 - 打开当前 WiFi 的静态 IP 设置页面 - 查看当前连接的 WiFi 信息 - 查看当前连… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_wifi_p_2_p_settings_activity` | 打开/进入P2P连接页面。该功能不直接进行连接操作。该页面可以查看搜索到的所有支持P2P的设备，并且可以发起连接申请。 ｜正例： - 打开P2P连接页面 - 查看支持P2P的设备 - 我要发起P2P设备连接 - 打开无线直连页面 - 查看无线直连设备 - 连接无线直连设备 - 查看无线直连设备状态 ｜反例： - 打开W… | LOCAL | APP_SIGN |
| `connectivitysettings_open_settings_wifi_settings_activity` | 打开系统设置中的 WiFi 设置页（WiFi 列表和配置入口）。 ｜正例： - 打开 WiFi 设置 - 进入 WiFi 设置 - 打开 WiFi 页面 - 进入 WiFi 页面 - 搜索 WiFi 网络 ｜反例： - 打开 WiFi 高级设置 → 应走 connectivitysettings_open_settin… | LOCAL | APP_SIGN |

## 时钟

`com.android.alarmclock`　·　10 项能力　·　世界时钟，定时器

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `alarm_clock_add` | 创建新闹钟 ｜正例： - 帮我定一个早上七点的闹钟 - 设置一个明天上班前的闹钟 - 给我加一个每个工作日都会响的闹钟 - 帮我设一个每周一早上八点的闹钟 - 定一个周六周日都会响的闹钟 - 定一个标题叫「早起」的七点闹钟 - 定一个闹钟，标题是「早起」、周四的九点半闹钟 - 定一个会震动的闹钟 ｜反例： - 删除早上… | LOCAL | APP_SIGN |
| `alarm_clock_delete` | 按小时和分钟删除已有闹钟 ｜正例： - 删除早上七点半的闹钟 - 把八点的闹钟删掉 - 删除晚上九点十五分的闹钟 ｜反例： - 删除所有闹钟 → 应走 alarm_clock_delete_all - 关闭所有闹钟 → 应走 alarm_clock_disable - 关闭早上七点的闹钟 → 应走 alarm_cloc… | LOCAL | APP_SIGN |
| `alarm_clock_delete_all` | 永久删除所有闹钟。此操作无法撤销。 ｜正例： - 把所有闹钟都删掉 - 清空我的闹钟 - 永久删除全部闹钟 ｜反例： - 删除早上那个闹钟 → 应走 alarm_clock_delete - 把所有闹钟都停用 → 应走 alarm_clock_disable | LOCAL | APP_SIGN |
| `alarm_clock_disable` | 停用所有闹钟 ｜正例： - 把所有闹钟都关掉 - 停用全部闹钟 - 关闭所有已设置的闹钟 ｜反例： - 删除所有闹钟 → 应走 alarm_clock_delete_all - 关闭早上七点的闹钟 → 应走 alarm_clock_disable_one | LOCAL | APP_SIGN |
| `alarm_clock_disable_one` | 按小时和分钟停用已有闹钟（不删除，可再次开启） ｜正例： - 关闭早上七点的闹钟 -关闭八点的闹钟 - 把八点的闹钟关掉 - 停用晚上九点十五分的闹钟 ｜反例： - 关闭所有闹钟 → 应走 alarm_clock_disable - 删除早上七点的闹钟 → 应走 alarm_clock_delete | LOCAL | APP_SIGN |
| `alarm_clock_get_current_time_by_city` | 获取应用列表中某个世界时钟城市的当前时间（可使用该城市的城市 id、本地化/英文名称或已配置的时区字符串） ｜正例： - 查一下伦敦现在几点 - 帮我看北京当前时间 - 查询 Tokyo 的现在时间 - 看看 C256 这个世界时钟城市的当前时间 ｜反例： - 查一下我现在所在位置的时间和时区 → 应走 alarm_c… | LOCAL | APP_SIGN |
| `alarm_clock_get_current_time_zone` | 获取当前时间、当前位置和当前时区信息。 ｜正例： - 现在几点了？ - 我现在在哪个时区？ - 帮我看一下当前时间和时区。 - 获取我当前位置的时间信息。 ｜反例： - 查一下某个城市现在几点。 → 应走 alarm_clock_get_current_time_by_city ｜返回： json对象 | LOCAL | APP_SIGN |
| `alarm_clock_get_enable` | 获取时钟应用中所有已启用的闹钟。 ｜正例： - 帮我看看现在开启了哪些闹钟 - 查看所有已启用的闹钟 - 有哪些闹钟是打开状态 ｜返回： 可读文案，例如：您开启了15：00，0：35，共计2个闹钟 | LOCAL | APP_SIGN |
| `alarm_clock_snooze` | 使用每个闹钟配置的稍后提醒时长，推迟所有当前正在响铃的闹钟；无法稍后提醒的闹钟会被视为已错过；仅影响正在响铃的闹钟。 ｜正例： - 把正在响的闹钟稍后提醒 - 闹钟先贪睡一下 - 所有正在响的闹钟都延后提醒 ｜反例： - 禁用所有闹钟 → 应走 alarm_clock_disable - 删除所有闹钟 → 应走 ala… | LOCAL | APP_SIGN |
| `alarm_clock_timer_add` | 启动一个新的倒计时计时器，并按指定秒数进行倒计时。 ｜正例： - 帮我启动一个十分钟倒计时 - 设置一个做饭用的倒计时 - 开一个倒计时计时器 ｜反例： - 帮我设一个明早响的闹钟 → 应走 alarm_clock_add | LOCAL | APP_SIGN |

## 高德云端MCP

云端服务　·　8 项能力　·　高德云端MCP

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `maps_direction_transit_integrated` | 高德公交/地铁路线规划。输入起终点经纬度与起终点城市（跨城时两城都必给），返回换乘方案 transits[]，每个方案 buslines[] 含线路名、乘坐距离、耗时、上下车站与途经站。 ## 坐标系 高德工具传入及返回的经纬度（包括卡片和导航链接中的坐标）均使用 GCJ-02（国测局坐标）。高德工具返回的坐标可直接传… | CLOUD | - |
| `maps_distance` | 高德两点间距离/耗时测量。输入起点（支持多个）与终点经纬度，按驾车/步行/直线三种方式返回 results[]（每条含 origin_id/dest_id/distance/duration）。调用逻辑：坐标从 maps_search_detail 获取；「A 到 B 多远/开车多久」这类问题用本能力，不需要完整路线时… | CLOUD | - |
| `maps_geo` | 高德地址转坐标（地理编码）。输入结构化门牌地址，返回 results[]（省市区 + location 坐标）。 ## 坐标系 高德工具传入及返回的经纬度（包括卡片和导航链接中的坐标）均使用 GCJ-02（国测局坐标）。高德工具返回的坐标可直接传给其他高德工具，无需再次转换。 ## 先反问（最高优先级） 目的地是私人住… | CLOUD | - |
| `maps_ip_location` | 高德 IP 定位。输入 IPv4 地址，返回其归属的省市、adcode 与大致范围。注意：ip 参数必须传具体 IP，传空字符串不会自动使用本机 IP（会返回空字段）。查用户当前位置不要用本能力，用系统的 get_current_location。 ## 坐标系 高德工具传入及返回的经纬度（包括卡片和导航链接中的坐标）… | CLOUD | - |
| `maps_regeocode` | 高德坐标转行政区划（逆地理编码）。输入经纬度，返回国家/省/市/区。返回读取注意：解析后直接是 {country,province,city,district} 对象，没有 results 包裹层；直辖市（北京/上海/天津/重庆）的 city 字段是空数组而非字符串，呈现时回退用 province。 ## 坐标系 高德… | CLOUD | - |
| `maps_schema_personal_map` | 生成高德 App 地图链接，把已确定的一批地点或多点行程标到高德 App 地图上给用户看。返回 amapuri://workInAmap/createWithToken 链接，用户点击后在高德地图查看。【何时用】仅当用户明确要在高德 App 地图中查看已确定地点的分布或行程标点、不要求导航时使用。用户要求「先去 A 再… | CLOUD | - |
| `maps_search_detail` | 高德 POI 详情查询。输入 maps_text_search 返回的 POI id，或 amap_overview_card 选定的结果项 poiId，返回该地点的完整信息：location（经纬度，GCJ-02）、地址、商圈、类型、评分、消费、营业时间、别名、等级、图片。调用逻辑：这是坐标的唯一可靠来源——任何需要… | CLOUD | - |
| `maps_text_search` | 高德关键词 POI 搜索。输入地点名/品牌/地标关键词，返回候选 POI 列表 pois[]（含 id、名称、地址、类型、图片；不含坐标）。 ## 坐标系 高德工具传入及返回的经纬度（包括卡片和导航链接中的坐标）均使用 GCJ-02（国测局坐标）。高德工具返回的坐标可直接传给其他高德工具，无需再次转换。本工具不返回经纬… | CLOUD | - |

## 滴滴

云端服务　·　7 项能力　·　滴滴出行打车

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `didi_auth_card` | 滴滴出行授权与开通入口（唯一推荐入口）。先查用户是否已授权、是否已开通免密/智能叫车，再按结果返回「去授权」卡、「去开通」卡，或纯文本「已授权完成」。 ## 何时使用 - 用户说：滴滴授权、绑定滴滴、登录滴滴、开通滴滴、开通免密支付、开通智能叫车 - 用户问：我授权滴滴了吗、滴滴能不能打车、是否开通免密 - 打车能力返… | CLOUD | - |
| `didi_auth_revoke` | 取消/撤销滴滴出行授权。清除本地滴滴凭证，调用前会先查是否已授权：未授权则直接返回「无需取消」 ## 硬性约束 - 这个原子能力是云端能力，不能通过node.invoke方式调用，必须 cloud=true调用 - 如果滴滴授权执行失败，先 search获取最新描述 再 exe ## 何时使用（必须命中这些意图） - … | CLOUD | - |
| `didi_taxi_cancel_order` | 提交取消指定滴滴进行中订单的请求，接受本平台 order_id 和取消原因。返回取消结果或当前不可取消状态；成功执行会改变订单状态 | CLOUD | - |
| `didi_taxi_create_order` | 使用滴滴有效估价标识和所选车型价格创建订单并开始匹配司机，返回 orderId 和订单状态。成功执行会产生真实订单；请求超时时执行结果可能未知 | CLOUD | - |
| `didi_taxi_estimate` | 按起终点城市与地址查询滴滴可用车型和预估价格，支持内部地点解析。返回匹配的起终点、车型价格及本次估价标识 traceId，供创建订单使用。授权或免密条件未满足时返回相应状态或卡片 | CLOUD | - |
| `didi_taxi_get_driver_location` | 获取司机实时经纬度。**仅在 `statusCode` 为 `1`/`2`/`4` 阶段有效**——其他状态会报 `-32011`。 **前置**：用 `didi_auth_status` 查询授权状态；`orderId` 用 `didi_taxi_create_order` 拿到；先用 `didi_taxi_quer… | CLOUD | - |
| `didi_taxi_query_order` | 查询滴滴订单状态及该阶段可用的司机、接驾距离和预计到达时间等信息。order_id 可指定本平台订单；省略时查询当前账号的未完成订单。本接口不创建新订单 | CLOUD | - |

## 权限控制器

`com.android.permissioncontroller`　·　6 项能力　·　摄像头、麦克风、位置权限管理；照片和文件删除保护管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `security_permissioncontroller_delete_file_and_image_protect` | 开启或关闭安全中心/权限管理中的「照片和文件删除保护」开关，以控制对照片、文件删除操作的限制或放行。当用户要开启「照片和文件删除保护」时传enable=【true】；当用户要关闭「照片和文件删除保护」时传 enable=【false】。 ｜正例： - 打开照片删除保护 - 关闭文件删除保护 - 别让照片被删 - 开启照… | LOCAL | APP_SIGN |
| `security_permissioncontroller_enter_file_recycle_bin_page` | 对文件管理/文件应用中的「回收站」页面进行跳转进入，用于查看已删除的文件并进行恢复或彻底清理。 ｜正例： - 打开文件回收站 - 进入文件回收站 - 带我去文件的回收站 - 看看我删的文件 - 去已删除文件那里 ｜反例： - 打开照片回收站 → 应走 security_permissioncontroller_ente… | LOCAL | APP_SIGN |
| `security_permissioncontroller_enter_image_recycle_bin_page` | 对相册/图库中的「回收站」页面进行跳转进入，用于查看已删除的照片/视频并进行恢复或彻底清理。 ｜正例： - 打开图库回收站 - 进入照片回收站 - 带我去相册回收站 - 看看最近删的照片 - 照片回收站里有什么 ｜反例： - 打开文件回收站 → 应走 security_permissioncontroller_ente… | LOCAL | APP_SIGN |
| `security_permissioncontroller_global_camera` | 开启或关闭系统级摄像头总开关，控制系统摄像头是否可以正常使用。本能力仅控制系统全局摄像头总开关总开关，关闭后所有应用均无法使用摄像头；单个/某个应用的相机/摄像权限不由本能力控制，不支持允许或禁止某个应用使用摄像头，无法影响单个/某个应用能否使用摄像头的权限。。 ｜正例： - 打开摄像头总开关 - 关闭系统摄像头开关 … | LOCAL | APP_SIGN |
| `security_permissioncontroller_global_location` | 开启或关闭系统级位置信息（GPS/定位）总开关，控制系统位置信息（GPS/定位）是否可以正常使用。本能力仅控制系统全局位置信息（GPS/定位）总开关，关闭后所有应用均无法使用位置信息（GPS/定位）；单个/某个应用的位置信息（GPS/定位）权限不由本能力控制，不支持允许或禁止某个应用使用位置信息（GPS/定位），无法影… | LOCAL | APP_SIGN |
| `security_permissioncontroller_global_microphone` | 开启或关闭系统级麦克风总开关，控制系统麦克风是否可以正常使用。本能力仅控制系统全局麦克风总开关，关闭后所有应用均无法使用麦克风；单个/某个应用的麦克风权限不由本能力控制，不支持允许或禁止某个应用使用麦克风，无法影响单个/某个应用能否使用麦克风的权限。 ｜正例： - 打开麦克风总开关 - 关闭系统麦克风 - 禁用麦克风 … | LOCAL | APP_SIGN |

## 快记

`com.android.soundrecorder`　·　5 项能力　·　录音

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `lite_recorder_open_home` | 打开快记 App 并进入首页。不具备录音转文字能力。 ｜正例： - 打开快记 - 打开快记首页 - 帮我进入快记 ｜反例： - 打开快记开始录音 → 应走 lite_recorder_open_recording | LOCAL | APP_SIGN |
| `lite_recorder_open_recording` | 打开快记并进入录音功能。若缺少麦克风或音乐和音频等录音所需权限，会先引导用户在快记内完成授权（返回等待授权，不要说成已成功开启）；授权完成后再自动开始录音。不具备录音转文字能力。 ｜正例： - 开始录音 - 打开快记开始录音 - 帮我录音 - 我要用快记录一段 ｜反例： - 打开快记首页 → 应走 lite_recor… | LOCAL | APP_SIGN |
| `lite_recorder_pause_recording` | 暂停当前正在进行的录音。正在手动录音时暂停手录；已是暂停态则成功返回并说明已暂停。当前没有可暂停的录音时返回失败（资源缺失），须明确告知用户当前没有可暂停的录音，不要说成已暂停成功。凡表达暂停录音、先停一下（但不要结束保存），均走本能力。不具备录音转文字能力。 ｜正例： - 暂停录音 - 先暂停一下录音 - 帮我把录音… | LOCAL | APP_SIGN |
| `lite_recorder_resume_recording` | 恢复当前已暂停的录音。手动录音处于暂停时继续手录；已在录则成功返回并说明已在进行中。当前没有可恢复的录音时返回失败（资源缺失），须明确告知用户当前没有可恢复的录音，不要说成已恢复成功。凡表达继续录音、恢复录音、接着录，均走本能力。不具备录音转文字能力。 ｜正例： - 继续录音 - 恢复录音 - 接着录 - 帮我把录音继… | LOCAL | APP_SIGN |
| `lite_recorder_stop_recording` | 结束当前录音或当前这一段对话录制。正在手动录音时结束并保存；当前没有可结束的录音时也成功返回。凡表达停止/结束录音、结束这一段（对话）录制，均走本能力。「保存录音」同样走本能力，直接结束并保存当前这一段，不要翻存储或反问。不具备录音转文字能力。 ｜正例： - 结束录音 - 结束录制这一段对话 - 结束这一段录制 - 停… | LOCAL | APP_SIGN |

## 系统界面助手

`com.stepos.systemuiex`　·　4 项能力　·　录屏与截屏

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `screen_capture_record` | 启动屏幕录制功能，用于启动当前屏幕录制并录制设备屏幕视频。支持通过开始录屏、屏幕录像、录制屏幕等方式触发。 ｜正例： - 帮我开始录屏 - 录制一下当前屏幕 - 开启屏幕录制 - 屏幕录像 - 录制屏幕 ｜反例： - 停止录屏 → 应走 screen_capture_stop_record | LOCAL | APP_SIGN |
| `screen_capture_screenshot` | 用于捕获当前设备屏幕内容，截屏 ｜正例： - 帮我截个屏 - 截取当前屏幕 - 把现在的屏幕截图保存一下 ｜反例： - 帮我截一张长图 → 应走 screen_capture_take_long_screenshot - 给这个页面滚动截图 → 应走 screen_capture_take_long_screensho… | LOCAL | APP_SIGN |
| `screen_capture_stop_record` | 停止屏幕录制功能，用于结束当前正在进行的屏幕录制任务并保存视频文件。无需进入设置页面即可直接停止录屏。 ｜正例： - 停止录屏 - 结束当前的屏幕录制 - 帮我关闭录制并保存视频 ｜反例： - 开始录屏 → 应走 screen_capture_record - 帮我录一下屏幕 → 应走 screen_capture_r… | LOCAL | APP_SIGN |
| `screen_capture_take_long_screenshot` | 长截图功能，用于自动滚动当前页面并连续截图，拼接生成完整长图。适用于网页、聊天记录、列表等超出屏幕范围的内容截取场景。截长图。 ｜正例： - 帮我截一张长截图 - 把当前页面滚动截完整 - 给这个聊天记录做长截图 - 截取完整页面 ｜反例： - 帮我截一下当前屏幕 → 应走 screen_capture_screens… | LOCAL | APP_SIGN |

## 什么值得买

云端服务　·　4 项能力　·　值得买开发的海纳购物管家，一款专业为用户提供来自全网与兴趣高度相关的、公允的AI消费决策支持工具。它支持四种消费决策模式：商品推荐、商品总结、商品对比、优惠好价。

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `zhidemai_content_search` | 用于查询商品的真实使用体验、评测、口碑、优缺点和选购攻略。 检索值得买社区、知乎、微信、今日头条、B站等平台的评测及消费经验文章，支持通过 'data_source' 限定来源平台。 调用场景：用户想了解“实际用起来怎么样”“有哪些缺点”“大家怎么评价”“怎么选、有哪些坑”。 边界：用户直接要求推荐一款或几款具体商品时… | CLOUD | - |
| `zhidemai_discount_search` | 用于查询优惠爆料及优惠购买方案。 检索值得买用户爆料的当前优惠，返回爆料价、领券步骤、凑单加购指引和直达购买链接。 调用场景：用户明确询问“有没有优惠券”“最近有什么好价”“怎么领券”“怎么凑单”“优惠怎么叠加”。 边界：单纯查询当前售价、跨商城比价或推荐具体商品，优先使用 zhidemai_product_searc… | CLOUD | - |
| `zhidemai_graph_search` | 用于查询商品的客观参数、规格和型号配置差异。 在知识图谱中查询3C数码、家电等商品实体，返回产品描述、核心参数、热度值及相关文章链接，支持按领域限定范围。 调用场景：用户询问“参数是多少”“有哪些配置”“两个型号的规格有什么区别”。 边界：“实际续航怎么样”“好不好用”“有哪些缺点”属于使用体验，优先使用 zhidem… | CLOUD | - |
| `zhidemai_product_search` | 用于查找、筛选和推荐可购买的具体商品，以及查询当前售价、进行跨商城比价。 按品类或商品关键词检索淘宝、京东、天猫、拼多多等商城的SKU列表，返回价格、销量、规格、店铺及历史价格标签，支持按商城ID、品牌、价格区间和排序方式筛选。 调用场景：用户要求“推荐一款/几款商品”“找符合条件的商品”“查各平台价格”“按价格或销量… | CLOUD | - |

## WorkBuddy MCP

云端服务　·　4 项能力　·　通过外部agent服务封装MCP服务跟WorkBuddy进行通信

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `wb_chat` | 发起一轮对话（异步）。立即返回 session_id/run_id/message_id 回执；真正回答稍后经 wb_get_session_history 轮询该 run 的 response 终帧。 | CLOUD | - |
| `wb_get_file_sync` | 按 file_id 取产物下载/预览 URL（异步轮询用）。file_status: 0 同步中 / 1 已同步 / 2 失败 / 3 安审；同步中时调用方应继续轮询。 | CLOUD | - |
| `wb_get_run_status` | 按 session_id + run_id 查询单轮执行状态与结果（异步轮询用）。status: RUN_CREATED 创建成功 / RUN_RUNNING 执行中 / RUN_FAILED 失败 / RUN_TIMEOUT 超时 / RUN_SUCCESS 成功；成功时 result 为终帧 assistant M… | CLOUD | - |
| `wb_get_session_history` | 按 session_id 拉该会话全部 run 的终帧记录（异步轮询用）。completed=false 表示该 run 尚未产出回答，调用方应继续轮询。since_seq/limit 支持增量与分页。 | CLOUD | - |

## 软件包安装程序

`com.android.packageinstaller`　·　3 项能力　·　恢复删除系统应用，卸载应用

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `security_packageinstaller_install_calendar` | 在系统安装器中恢复或重新安装系统日历应用，用于误删后找回预装日历。 ｜正例： - 找回系统日历 - 恢复系统日历 - 把系统日历装回来 - 重新安装日历 - 日历被删了帮我恢复 | LOCAL | APP_SIGN |
| `security_packageinstaller_install_filemanager` | 在系统安装器中恢复或重新安装系统文件管理器应用，用于误删后找回预装文件管理器。 ｜正例： - 找回文件管理器 - 恢复系统文件管理 - 把文件管理装回来 - 重新安装文件管理器 - 文件管理被删了帮我恢复 | LOCAL | APP_SIGN |
| `security_packageinstaller_uninstall` | 在系统安装器中按应用名称卸载已安装应用，适用于清理不再使用的软件。 ｜正例： - 卸载微信 - 把抖音删掉 - 删除这个应用 - 移除支付宝 - 把这个软件卸了 | LOCAL | APP_SIGN |

## 携程

云端服务　·　3 项能力　·　携程航班搜索、酒店搜索、火车票搜索、景点搜索、旅行规划、旅行攻略

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `query_flight` | 查询航班机票信息。该工具支持通过出发/到达城市名称或城市三字码查询机票和航班信息，可结合出发日期、机场、航司、舱位、价格、直飞/中转、起飞/到达时段等条件筛选，并可按价格或出发时间排序。结果包含航空公司、航班号、起降机场、起降时间、飞行时长、舱位、票价、折扣及余票提示等信息。\n\n 适用于“查机票”“北京飞上海明天有… | CLOUD | - |
| `query_hotel` | 全市酒店标签检索，必须配合 cityName，每次只能传一个标签。 禁止与 landmarkName、longitude/latitude、hotelName 同时传入：一旦带 tags，上游会忽略位置条件，按全市该标签召回。例如「南京 + 河西 + 精品民宿」会返回汤山/夫子庙一带的民宿，而不是河西/奥体附近。 用户… | CLOUD | - |
| `query_train` | 查询携程火车票信息。该工具可根据出发城市、到达城市及出发日期查询火车车次，支持直达与中转方案；可按车型、车站、席别、余票、出发/到达时段等条件筛选，并可按价格、发车时间、运行时长排序。结果包含车次、出发/到达时间、出发/到达车站、运行时长、席别价格、余票情况及列车标签等信息。\n\n适用于“查火车票”“北京到上海明天的… | CLOUD | - |

## 高德

云端服务　·　3 项能力　·　高德唤端链接拼接（ai-tools /amap，步行/骑行导航 deeplink）

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `amap_overview_card` | 高德地图概览卡聚合能力。输入搜索关键词（可选中心点/城市），搜索一批地点并在服务端补齐坐标，返回端侧可直接渲染的地图概览卡（map_poi_list）：一张地图上按序标注多个地点，列表每项含名称、评分、距离、分类标签，可展开看营业时间/图片/人均等详情。 ## 坐标系 高德工具传入及返回的经纬度（包括卡片和导航链接中的… | CLOUD | - |
| `amap_poi_detail_card` | 高德地点详情卡聚合能力。输入 place（具体地点名、地址或真实高德 POI ID），工具内部解析地点并拉取详情，无需事先调用搜索能力，返回端侧可直接渲染的地点详情卡（map_poi_detail）：名称、评分、地址、商圈、营业时间、人均消费、图片，卡上带「导航过去」按钮。 ## 坐标系 高德工具传入及返回的经纬度（包… | CLOUD | - |
| `amap_route_card` | 高德出行路线卡聚合能力。直接传 origin、destination，两端分别支持 GCJ-02 坐标、具体地点名/地址或真实高德 POI ID（poi:ID 或裸 ID），可混用；工具内部完成地点搜索、获取坐标和路线查询，不必事先调用地点搜索或详情能力。一次并发拉取驾车/步行/骑行三种方式的耗时与距离，返回端侧可直接… | CLOUD | - |

## 私密保险箱

`com.stepos.safebox`　·　2 项能力　·　用户个人文件加密管理器

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `security_safebox_auto_fill` | 在 设置 的安全相关能力中，针对「私密保险箱」开启、关闭或查询自动填充：开启后符合条件时可自动填入保险箱内保存的密码或账号信息，关闭后需手动输入。未传 enable 时查询当前开关状态。 ｜正例： - 打开私密保险箱自动填充 - 打开私密保险箱中的自动填充 - 打开私密保险箱的自动填充 - 关掉保险箱自动填充 - 让保… | LOCAL | APP_SIGN |
| `security_safebox_open` | 在 设置 中跳转到「安全」下的「私密保险箱」页面，便于管理加密相册、文件、密码等保险箱内容与相关选项。 ｜正例： - 打开私密保险箱 - 进保险箱设置 - 去哪找私密保险箱 - 打开设置里安全中的保险箱 - 我想设置私密保险箱 - 私密保险箱在哪 ｜反例： - 开启私密保险箱自动填充 → 应走 security_saf… | LOCAL | APP_SIGN |

## Log Report

`com.stepos.logreport`　·　2 项能力　·　系统log日志抓取与停止

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `start_record_log` | Launch feedback application. | LOCAL | APP_SIGN |
| `stop_record_log` | Performs no operation. | LOCAL | APP_SIGN |

## 安全服务

`com.stepos.secureservice`　·　2 项能力　·　系统底层服务，获取手机标识码，OAID,UUID等

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `security_service_get_uuid` | 在安全服务宿主场景下查询并返回当前设备的 OAID（匿名设备标识）；无入参，由端侧直接返回结果。｜正例： - 手机 OAID 是多少 - 匿名设备标识是什么 - 查一下 OAID - 广告标识符是多少 - 本机 OAID 帮我查 ｜反例： - 打开 OAID 设置 → 应走 security_service_open_… | LOCAL | APP_SIGN |
| `security_service_open_oaid_settings` | 在安全服务宿主场景下拉起系统侧 OAID（匿名设备标识）设置界面，用户可查看说明、关闭或调整广告标识相关开关，以及管理应用对设备标识的访问。 ｜正例： - 打开 OAID 设置 - 设备标识在哪改 - 广告标识符怎么关 - 带我去匿名设备标识那一页 - 系统里设备匿名标识入口在哪 ｜反例： - 获取当前设备的 UUID… | LOCAL | APP_SIGN |

## 搜索

`com.stepos.net.search`　·　2 项能力

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `search_open` | 打开全局搜索页面，支持搜索应用和设置项 ｜正例： - 打开全局搜索 - 帮我打开全局搜索 - 我想搜索应用/app ｜反例： - 打开搜索设置 → 应走 search_setting | LOCAL | APP_SIGN |
| `search_setting` | 打开全局搜索的设置页面，路径为全局搜索—更多—设置 ｜正例： - 打开全局搜索的设置页 - 帮我打开全局搜索的设置页 - 进入全局搜索的设置页 ｜反例： - 打开全局搜索 → 应走 search_open | LOCAL | APP_SIGN |

## 相机

`com.stepos.media.camera`　·　2 项能力

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `camera_open_beauty_mode` | 打开相机美颜模式：拉起相机并开启美颜，保持当前默认摄像头和拍摄模式。例如：打开美颜、开启美颜、美颜模式。本能力只拉起相机并开美颜、不拍照。以下说法不走本能力：切换到人像模式、调到某个拍摄模式（人像/夜景/慢动作等） → 应走 camera_switch_mode。 | LOCAL | APP_SIGN |
| `camera_open_selfie_mode` | 打开相机自拍模式：拉起相机并使用前置镜头进入自拍场景，保持当前拍摄模式不变。例如：自拍、打开自拍、我要自拍、自拍一张。本能力只进入自拍场景、不拍照；「自拍一张」需再走 camera_capture 拍照。本能力只处理「自拍」这个场景意图。如果用户说的是切换镜头的动作——切换到前置摄像头、切换到后摄、调到前置/后置、翻转… | LOCAL | APP_SIGN |

## 系统界面

`com.android.systemui`　·　1 项能力　·　手机锁屏、解锁界面，通知查看

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `open_flash_light` | 打开或关闭闪光灯 ｜正例： - 打开闪光灯 - 关掉闪光灯 - 帮我开一下手电筒 - 把手电筒关了 | LOCAL | APP_SIGN |

## 帮助和反馈

`com.stepos.feedback`　·　1 项能力　·　提交手机使用的问题反馈

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `feedback_submit_question` | 通过 AI 对话提交用户的问题反馈到帮助与反馈系统，并自动上传系统收集的设备信息（如机型、系统版本、固件版本、地理位置等）。提交成功返回「提交成功」，失败返回具体错误原因。 ｜正例： - 我要反馈一个问题 - 帮我提交一下使用中遇到的故障 - 我想给帮助和反馈提个建议 - 把我刚才描述的问题反馈给工程师 | LOCAL | APP_SIGN |

## XMSCore

`com.stepos.xmscore`　·　1 项能力　·　系统服务，可获取位置信息

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `get_current_location` | 在系统定位服务中查询你当前所在位置，返回当前位置的经纬度和文字地址（国家、省、市、区县及完整地址）。latitude/longitude 为 WGS84（与 Android 原生 GPS 一致）。国内网约车、高德、腾讯、滴滴请使用 gcjLatitude/gcjLongitude（GCJ-02），不要把 WGS84 当… | LOCAL | APP_SIGN |

## 计算器

`com.stepos.calculator`　·　1 项能力　·　计算器，用于进行数学计算

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `evaluate_expression` | 根据数学表达式字符串计算结果，与计算器内置科学计算引擎一致（Arity）；三角函数默认按角度，可通过 use_radians 切换为弧度。 ｜正例： - 帮我算一下二加三乘四等于多少 - 用计算器算 sin 三十 - 帮我算根号二 - 按弧度帮我算一下三角函数 ｜返回： 成功时返回 MCP CallToolResult… | LOCAL | APP_SIGN |

## 应用商店

`com.stepos.appstore`　·　1 项能力　·　应用查询、下载、管理及更新等

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `appstore_search_app` | 在应用商店里**搜索 / 查询 / 查找**应用——跳到商店搜索页并自动按关键词检索，结果由商店 原生页面展示。**只查询，不下载、不安装**； **动词归一化**：搜索 / 搜 / 查询 / 查 / 查找 / 找 / 看看有没有 / 应用商店里有没有 → 本函数。 ｜正例： - 在应用商店搜一下咪咕音乐 - 帮我搜索… | LOCAL | APP_SIGN |

## Amoo

`com.stepos.ailauncher`　·　1 项能力　·　手机桌面，小跃AI配置管理

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `ailauncher_load_tripartite_common_card` | 用途：当你已经拿到一条来自第三方平台的结构化业务结果，需要在聊天界面里以一张「卡片」的形式直观展示给用户时，调用本能力。它会把你给的字段渲染成带标题/状态/摘要/跳转按钮的可视卡片，比纯文字回复更清晰，用户可直接在卡片上点按钮跳转到对应三方 App 或网页。 何时使用：手里有需要可视化展示的三方业务数据，且希望用户能一… | LOCAL | APP_SIGN |

## 智能体安全中心

`com.stepos.agentsafetycenter`　·　1 项能力　·　端侧openclaw敏感行为权限请求显示

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `file_restore` | 按删除前的外部存储原始路径从回收站恢复文件或目录。目录恢复默认包含原路径前缀下的项目；recursive=false 时只恢复精确匹配路径。path 与 paths 互斥，必须二选一传入。 ｜正例： - 恢复这个文件 - 把刚才删除的目录还原 - 按原来的路径从回收站恢复文件 ｜反例： - 把文件移到回收站 → 应走 … | LOCAL | APP_SIGN |

## 天气

`com.stepos.weather`　·　1 项能力

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `weather_get_current_location_weather` | 查询用户当前所在地的天气（端内自动定位，需定位权限与已同意隐私政策）,返回逐日或者逐时的天气信息,并以卡片形式向用户展示详细数据。 [type]类型说明： - `by_date`（默认）：按日期的逐天 - `by_hour`：按小时，返回[startDate]当天全部可用逐时 + 次日 00:00~07:00（共 8 … | LOCAL | APP_SIGN |

## 咪咕音乐

云端服务　·　1 项能力　·　咪咕音乐MCP服务

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `music_recommend` | 根据用户输入的歌名、关键词、歌手、心情或场景，从咪咕音乐曲库推荐若干首歌曲，返回歌名、歌手、封面图及可直接播放的歌曲链接。 - 调用本能力推荐音乐后，可直接在Amoo界面展示音乐推荐的交互式卡片。因此模型无需再次总结或输出音乐推荐结果 - 调用本能力推荐音乐后，本能力的交互式卡片中自带播放按钮，请**不要**继续调用o… | CLOUD | - |

## 云端天气服务

云端服务　·　1 项能力　·　云端天气服务

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `get_weather` | 按三级行政区（province / city / area）查询未来15天内的天气数据，返回逐日或逐时的天气信息：daily（日级预报，按日期区间过滤）、hourly（逐时预报，仅 by_hour 时非 null）、realtime（实况，含空气质量 + 生活指数，仅日期范围含今天时非 null）、alerts（气象预… | CLOUD | - |

## 财跃AI

云端服务　·　1 项能力　·　通过财跃做金融信息查询

| 能力 | 说明 | 执行 | 鉴权 |
|---|---|---|---|
| `caiyue-ai-chat` | 财联社/财跃（AI小财神）金融信息查询与分析：支持个股基础行情（股价、涨跌幅、成交量、市值）、K线数据、个股及行业新闻、券商研报检索与摘要、基础财经知识问答和股票基础分析。 ## 何时调用 - 品牌触发：财联社、财跃、财跃AI、AI财跃、AI小财神（含带空格写法）、小财神。用户点名这些品牌查询上述金融信息，或要求分析、… | CLOUD | - |
