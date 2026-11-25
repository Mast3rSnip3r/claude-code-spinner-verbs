# claude-code-spinner-verbs

Custom spinner verbs for [Claude Code](https://github.com/anthropics/claude-code) — 888+ verbs across themed categories, with **automatic daily rotation**.

## ✨ Features

- **888+ verbs** across 32 themed categories
- **Daily auto-rotation** — a new category every day, shuffled per cycle so you never get the same one twice in a row
- **Works in CLI and VS Code** — updates both `~/.claude/settings.json` and VS Code's `settings.json`
- **Easy to customize** — edit `categories.json` to add/remove categories or verbs
- **Install in one command**

## 🚀 Quick Install

```bash
# Clone and run the installer
git clone git@github.com:Mast3rSnip3r/claude-code-spinner-verbs.git
cd claude-code-spinner-verbs
./install.sh
```

That's it. The next time you start Claude Code, you'll get a random category. The `rotate.py` script runs on every `SessionStart` hook to pick a new category for the day.

## 📦 What Gets Installed

| File | Purpose |
|------|---------|
| `categories.json` | All your verb categories (edit this to customize) |
| `rotate.py` | Daily rotation logic — runs on `SessionStart` |
| `install.sh` | Adds the hook and `spinnerVerbs` config to your `~/.claude/settings.json` |
| `uninstall.sh` | Removes everything cleanly |

## ⚙️ Manual Install (if you prefer)

1. Copy `categories.json` and `rotate.py` to `~/.claude/spinner-rotate/`
2. Add this to your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "python3 -I \"$HOME/.claude/spinner-rotate/rotate.py\" >/dev/null 2>&1 || true",
        "timeout": 10
      }]
    }]
  },
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": ["Loading..."]
  }
}
```

The `rotate.py` script will overwrite `spinnerVerbs` each day with today's category.

## 🎨 Customizing

Edit `categories.json` — it's a simple JSON object:

```json
{
  "My Category": ["Verb one", "Verb two", "Verb three"],
  "Another Category": ["First", "Second", "Third"]
}
```

- Category names are sorted alphabetically, then shuffled per cycle
- Each day gets one category; the cycle repeats after all categories are used
- The shuffle is deterministic per cycle (seeded), so you won't see repeats within a cycle

## 🔄 How Daily Rotation Works

- Categories are sorted → shuffled with a seed based on the cycle number (days since epoch / num_categories)
- Today's position in the cycle picks one category
- Next cycle uses a new seed → new shuffle order
- Adjacent-cycle boundary check ensures the last category of cycle N ≠ first of cycle N+1

## 🙏 Credits

This project was inspired by and builds on the excellent work by [wynandw87](https://github.com/wynandw87) in [claude-code-spinner-verbs](https://github.com/wynandw87/claude-code-spinner-verbs). The original category list and many verb ideas come from that repo — thank you!

The daily rotation script and install tooling are original additions.

## 📄 License

MIT — see [LICENSE](LICENSE). The verb lists are original creative work; the category *themes* (Simpsons, Star Wars, etc.) are pop-culture references used descriptively.