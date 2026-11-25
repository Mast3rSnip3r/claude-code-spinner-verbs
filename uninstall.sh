#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOTCLAUDE="$HOME/.claude"
SETTINGS="$HOME/.claude/settings.json"

echo "=== claude-code-spinner-verbs uninstaller ==="

# --- Remove categories.json and spinner-rotate ---
if [ -d "$DOTCLAUDE/spinner-rotate" ]; then
  echo "Removing spinner-rotate directory..."
  rm -rf "$DOTCLAUDE/spinner-rotate"
else
  echo "No spinner-rotate directory found"
fi

# --- Remove hook and spinnerVerbs from settings.json ---
if [ -f "$SETTINGS" ]; then
  echo "Removing hook and spinnerVerbs from settings.json..."
  python3 -c "
import json
with open('$SETTINGS', 'r') as f:
    cfg = json.load(f)
# Remove the spinner-rotate hook
hook_str = 'python3 -I \"\$HOME/.claude/spinner-rotate/rotate.py\" >/dev/null 2>&1 || true'
if 'hooks' in cfg and 'SessionStart' in cfg['hooks']:
    filtered = []
    for hook_group in cfg['hooks']['SessionStart']:
        new_hooks = [h for h in hook_group.get('hooks', []) if h.get('command') != hook_str]
        if new_hooks:
            hook_group['hooks'] = new_hooks
            filtered.append(hook_group)
    if filtered:
        cfg['hooks']['SessionStart'] = filtered
    else:
        del cfg['hooks']['SessionStart']
        if not cfg['hooks']:
            del cfg['hooks']
# Remove spinnerVerbs section
if 'spinnerVerbs' in cfg:
    del cfg['spinnerVerbs']
with open('$SETTINGS', 'w') as f:
    json.dump(cfg, f, indent=2)
    f.write('\\n')
print('settings.json cleaned up')
"
else
  echo "No settings.json found"
fi

# --- Also remove from VS Code settings if present ---
VSCODE_SETTINGS="$HOME/Library/Application Support/Code/User/settings.json"
if [ -f "$VSCODE_SETTINGS" ]; then
  echo "Removing claudeCode.spinnerVerbs from VS Code settings..."
  python3 -c "
import json
with open('$VSCODE_SETTINGS', 'r') as f:
    cfg = json.load(f)
if 'claudeCode.spinnerVerbs' in cfg:
    del cfg['claudeCode.spinnerVerbs']
    with open('$VSCODE_SETTINGS', 'w') as f:
        json.dump(cfg, f, indent=4)
        f.write('\\n')
    print('VS Code settings cleaned up')
"
fi

echo ""
echo "=== Uninstall complete! ==="
echo "Spinner verbs and rotation hook have been removed."
echo "You can delete this directory whenever you're ready."