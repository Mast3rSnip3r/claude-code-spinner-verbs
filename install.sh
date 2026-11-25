#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOTCLAUDE="$HOME/.claude"
SETTINGS="$HOME/.claude/settings.json"

echo "=== claude-code-spinner-verbs installer ==="

# --- Copy categories.json next to rotate.py (rotate.py reads it from its own dir) ---
mkdir -p "$DOTCLAUDE/spinner-rotate"
if [ ! -f "$DOTCLAUDE/spinner-rotate/categories.json" ] || [ "$DOTCLAUDE/spinner-rotate/categories.json" -ot "$SCRIPT_DIR/categories.json" ]; then
  echo "Installing categories.json ..."
  cp "$SCRIPT_DIR/categories.json" "$DOTCLAUDE/spinner-rotate/categories.json"
else
  echo "categories.json already exists, keeping existing"
fi

# --- Copy rotate.py if not already there ---
if [ ! -f "$DOTCLAUDE/spinner-rotate/rotate.py" ] || [ "$DOTCLAUDE/spinner-rotate/rotate.py" -ot "$SCRIPT_DIR/rotate.py" ]; then
  echo "Installing rotate.py ..."
  mkdir -p "$DOTCLAUDE/spinner-rotate"
  cp "$SCRIPT_DIR/rotate.py" "$DOTCLAUDE/spinner-rotate/rotate.py"
else
  echo "rotate.py already exists, keeping existing"
fi

# --- Update settings.json with the hook and spinnerVerbs ---
echo "Updating settings.json ..."
need_write=false

# Ensure spinnerVerbs section exists and has proper initial verbs
if [ ! -f "$SETTINGS" ]; then
  echo '{}' > "$SETTINGS"
  need_write=true
fi

# Read current settings
TMP_SETTINGS=$(mktemp)
python3 -c "
import json, sys
with open('$SETTINGS', 'r') as f:
    cfg = json.load(f)
# Set spinnerVerbs to a placeholder — rotate.py will overwrite on SessionStart
cfg['spinnerVerbs'] = {'mode': 'replace', 'verbs': ['Loading...']}
# Set hook to run rotate.py on SessionStart
if 'hooks' not in cfg:
    cfg['hooks'] = {}
if 'SessionStart' not in cfg['hooks']:
    cfg['hooks']['SessionStart'] = []
# Append the hook (avoid duplicates)
hook_str = 'python3 -I \"\$HOME/.claude/spinner-rotate/rotate.py\" >/dev/null 2>&1 || true'
found = False
for hook_group in cfg['hooks']['SessionStart']:
    for h in hook_group.get('hooks', []):
        if h.get('command') == hook_str:
            found = True
if not found:
    cfg['hooks']['SessionStart'].append({
        'hooks': [{
            'type': 'command',
            'command': hook_str,
            'timeout': 10
        }]
    })
with open('$SETTINGS', 'w') as f:
    json.dump(cfg, f, indent=2)
    f.write('\\n')
print('settings.json updated')
"

# Also ensure VS Code settings get updated (optional — let user decide)
echo ""
echo "=== Done! ==="
echo ""
echo "Your spinner verbs are now installed."
echo ""
echo "What happens next:"
echo "  1. On next Claude Code start, the SessionStart hook runs rotate.py"
echo "  2. rotate.py picks today's category and writes spinnerVerbs to your settings"
echo "  3. You'll see a random category's verbs as the spinner"
echo "  4. A new category appears each day (deterministic cycle, no repeats within a cycle)"
echo ""
echo "To customize categories, edit ~/.claude/categories.json"
echo "Run ./uninstall.sh to remove everything cleanly."