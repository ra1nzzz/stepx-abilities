#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日同步 STEPX Neo 原子能力清单。

流程：
  1. 拉取本机可见的全量原子能力列表；
  2. 与 data/abilities.json 逐条比对（新增 / 更新 / 移除）；
  3. 无变化 -> 直接退出，不产生提交；
  4. 有变化 -> 重写快照、刷新 snapshot.json、调用 render.py 重建文档、
     追加 CHANGELOG，提交并推送。

用法：
  python3 scripts/sync.py            # 正常同步
  python3 scripts/sync.py --dry-run  # 只比对，不写不推
"""

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "abilities.json"
SNAP_FILE = ROOT / "data" / "snapshot.json"
CHANGELOG = ROOT / "CHANGELOG.md"
CLI_CONFIG = Path(os.environ.get("ABILITY_CLI_CONFIG", "/root/.ability-cli/config.json"))
SERVICE_PATH = "/ability-service/api/agent/v1/ability/list"
CST = timezone(timedelta(hours=8))


def service_config():
    base = os.environ.get("ABILITY_SERVICE_BASE_URL")
    token = os.environ.get("ABILITY_SERVICE_TOKEN")
    device = os.environ.get("ABILITY_DEVICE_ID")
    if CLI_CONFIG.exists():
        cfg = json.loads(CLI_CONFIG.read_text(encoding="utf-8"))
        profile = (cfg.get("profiles") or {}).get(cfg.get("env", "prod"), {})
        defaults = cfg.get("defaults") or {}
        base = base or profile.get("baseUrl")
        token = token or profile.get("authToken")
        device = device or defaults.get("deviceId")
    if not base or not token:
        raise SystemExit("缺少原子能力服务地址或凭证")
    return base.rstrip("/"), token, device or ""


def fetch(base, token, device):
    url = "%s%s?deviceId=%s" % (base, SERVICE_PATH, urllib.parse.quote(device))
    req = urllib.request.Request(url, headers={
        "Authorization": token,
        "zy-device-id": device,
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=90) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    if body.get("code") not in (0, 200, "0", "200"):
        raise SystemExit("服务返回异常：code=%s msg=%s" % (body.get("code"), body.get("msg")))

    payload = body.get("data")
    if isinstance(payload, dict):
        payload = next((v for v in payload.values() if isinstance(v, list)), None)
    if not isinstance(payload, list):
        raise SystemExit("服务返回结构异常")
    return [x for x in payload if isinstance(x, dict) and x.get("abilityId")]


def fingerprint(items):
    blob = json.dumps(items, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


def item_key(item):
    return json.dumps(item, ensure_ascii=False, sort_keys=True)


def load_previous():
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []
    if isinstance(data, dict):
        data = data.get("data") or []
    return [x for x in data if isinstance(x, dict) and x.get("abilityId")]


def git(*args, check=True):
    proc = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise SystemExit("git %s 失败：%s" % (" ".join(args), proc.stderr.strip()))
    return proc.stdout.strip()


def append_changelog(day, added, updated, removed):
    lines = ["# 变更记录", ""]
    if CHANGELOG.exists():
        lines = [CHANGELOG.read_text(encoding="utf-8").rstrip("\n"), ""]
    lines += ["## %s" % day, ""]

    def block(title, rows):
        if not rows:
            return
        lines.append("- %s %d 项" % (title, len(rows)))
        for item in rows[:40]:
            lines.append("  - `%s`（%s）" % (item.get("name") or item.get("abilityId"), item.get("appName") or "未知"))
        if len(rows) > 40:
            lines.append("  - …共 %d 项" % len(rows))

    block("新增", added)
    block("更新", updated)
    block("移除", removed)
    CHANGELOG.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")


def main():
    dry_run = "--dry-run" in sys.argv
    base, token, device = service_config()
    current = sorted(fetch(base, token, device), key=lambda x: x["abilityId"])
    if not current:
        raise SystemExit("拉取到 0 条能力，疑似异常，已终止以保护现有快照")

    previous = sorted(load_previous(), key=lambda x: x["abilityId"])
    prev_map = {x["abilityId"]: x for x in previous}
    curr_map = {x["abilityId"]: x for x in current}

    added = [curr_map[i] for i in curr_map if i not in prev_map]
    removed = [prev_map[i] for i in prev_map if i not in curr_map]
    updated = [
        curr_map[i] for i in curr_map
        if i in prev_map and item_key(curr_map[i]) != item_key(prev_map[i])
    ]

    now = datetime.now(CST)
    print("拉取 %d 条；新增 %d，更新 %d，移除 %d" % (len(current), len(added), len(updated), len(removed)))

    if not (added or updated or removed):
        print("NO_CHANGE")
        return

    if dry_run:
        print("DRY_RUN 未写入")
        return

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    local = sum(1 for x in current if (x.get("callingMethod") or "").upper() == "LOCAL")
    cloud = sum(1 for x in current if (x.get("callingMethod") or "").upper() == "CLOUD")
    SNAP_FILE.write_text(json.dumps({
        "generated_at": now.isoformat(timespec="seconds"),
        "device": "STEPX Neo",
        "total": len(current),
        "local": local,
        "cloud": cloud,
        "apps": len({x.get("appName") or "未知" for x in current}),
        "content_sha256_16": fingerprint(current),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    render = subprocess.run([sys.executable, str(ROOT / "scripts" / "render.py")],
                            cwd=str(ROOT), capture_output=True, text=True)
    print(render.stdout.strip())
    if render.returncode != 0:
        raise SystemExit("render.py 执行失败：%s" % render.stderr.strip())

    append_changelog(now.strftime("%Y-%m-%d"), added, updated, removed)

    if not git("config", "user.name", check=False):
        git("config", "user.name", "ra1nzzz")
    if not git("config", "user.email", check=False):
        git("config", "user.email", "ra1nzzz@users.noreply.github.com")
    git("config", "http.version", "HTTP/1.1")

    git("add", "-A")
    git("commit", "-m", "sync %s: +%d ~%d -%d" % (now.strftime("%Y-%m-%d"), len(added), len(updated), len(removed)))

    last_error = ""
    for attempt in range(3):
        proc = subprocess.run(["git", "push", "origin", "HEAD"], cwd=str(ROOT), capture_output=True, text=True)
        if proc.returncode == 0:
            print("PUSHED")
            return
        last_error = proc.stderr.strip()
        time.sleep(10 * (attempt + 1))
    raise SystemExit("推送失败（提交已保留在本地）：%s" % last_error)


if __name__ == "__main__":
    main()
