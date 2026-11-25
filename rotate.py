#!/usr/bin/env python3
"""Set spinnerVerbs to today's category (one per day, shuffled cycle) for the CLI and the VS Code panel."""
import json, os, sys, tempfile, datetime, random
here = os.path.dirname(os.path.abspath(__file__))
settings = os.path.expanduser("~/.claude/settings.json")
vscode = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")
cats = json.load(open(os.path.join(here, "categories.json"), encoding="utf-8"))
names = sorted(cats)
today = datetime.date.today()
n = len(names)
cycle, pos = divmod(today.toordinal(), n)

def order(c):
    # Seeded shuffle: same order for the same cycle, no repeats within a cycle.
    o = names[:]
    random.Random(c).shuffle(o)
    # Avoid the same category on the last day of one cycle and the first day of the next.
    if c > 0:
        prev = names[:]
        random.Random(c - 1).shuffle(prev)
        if o[0] == prev[-1]:
            o[0], o[1] = o[1], o[0]
    return o

name = order(cycle)[pos]
want = {"mode": "replace", "verbs": cats[name]}

def write_json(path, cfg, indent):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".settings.")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=indent, ensure_ascii=False); f.write("\n")
    try:
        os.chmod(tmp, os.stat(path).st_mode & 0o777)
    except OSError:
        pass
    os.replace(tmp, path)

changed = False

# 1) Claude Code settings (CLI)
cfg = json.load(open(settings, encoding="utf-8"))
if cfg.get("spinnerVerbs") != want:
    cfg["spinnerVerbs"] = want
    write_json(settings, cfg, 2)
    changed = True

# 2) VS Code user settings (the chat panel reads claudeCode.spinnerVerbs from here).
#    Skipped if the file is missing or is not plain JSON (VS Code allows comments and trailing commas).
try:
    vcfg = json.load(open(vscode, encoding="utf-8"))
    if vcfg.get("claudeCode.spinnerVerbs") != want:
        vcfg["claudeCode.spinnerVerbs"] = want
        write_json(vscode, vcfg, 4)
        changed = True
except (OSError, ValueError):
    pass

if changed:
    print(f"spinnerVerbs -> {name} ({len(cats[name])} verbs) for {today}")
