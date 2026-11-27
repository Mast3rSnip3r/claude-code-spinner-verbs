#!/usr/bin/env python3
"""Generate README.md from categories.json so the counts and category lists never drift.

Usage: python3 scripts/build_readme.py   (run from the repo root)
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = os.path.join(ROOT, "categories.json")
README = os.path.join(ROOT, "README.md")


def slug(name):
    """GitHub-style heading anchor."""
    s = name.lower()
    s = re.sub(r"[^\w\- ]", "", s)  # keep letters, digits, _, -, space
    s = s.replace(" ", "-")
    return s


def cell(text):
    return text.replace("|", "\\|")


def main():
    with open(CATS, encoding="utf-8") as f:
        cats = json.load(f)

    names = sorted(cats)
    total = sum(len(cats[n]) for n in names)
    n_cats = len(names)

    out = []
    add = out.append

    add("# Claude Code Spinner Verbs — with Daily Rotation\n")
    add(
        f"A curated collection of **{total:,} spinner verbs** across **{n_cats} themed "
        "categories** for [Claude Code](https://github.com/anthropics/claude-code), with "
        "**automatic daily rotation** — Claude picks a new category every day.\n"
    )

    # ---- Table of contents ----
    add("## Table of Contents\n")
    add("| # | Category | Verbs |")
    add("|--:|----------|------:|")
    for i, n in enumerate(names, 1):
        add(f"| {i} | [{n}](#{slug(n)}) | {len(cats[n])} |")
    add("")

    # ---- How to use ----
    add("## How to Use\n")
    add(
        "Copy any category you like from the [Categories](#categories) section, then paste "
        "this prompt into Claude Code. Each category has a **Copy as list** dropdown with its "
        "verbs as quoted strings, ready to paste.\n"
    )
    add("```")
    add("Add the following spinner verbs to my ~/.claude/settings.json using \"mode\": \"append\":")
    add("")
    add("<paste the verbs here>")
    add("```\n")

    add("### Modes\n")
    add("| Mode | Behavior |")
    add("|------|----------|")
    add("| `\"append\"` | Add your verbs to Claude Code's built-in defaults |")
    add("| `\"replace\"` | Use only your verbs (the daily rotation uses this) |")
    add("")

    add("### Manual setup\n")
    add("Add a top-level `spinnerVerbs` key to `~/.claude/settings.json`:\n")
    add("```json")
    add("{")
    add('  "spinnerVerbs": {')
    add('    "mode": "append",')
    add('    "verbs": ["Second-breakfasting", "Silly-walking", "Great-scotting"]')
    add("  }")
    add("}")
    add("```\n")

    # ---- Install (daily rotation) ----
    add("## Daily Rotation (auto-install)\n")
    add(
        "This repo also ships a small rotation script that swaps in a new category each day, so "
        "the spinner stays fresh without you touching anything.\n"
    )
    add("```bash")
    add("git clone git@github.com:Mast3rSnip3r/claude-code-spinner-verbs.git")
    add("cd claude-code-spinner-verbs")
    add("./install.sh")
    add("```\n")
    add(
        "It copies `categories.json` and `rotate.py` into `~/.claude/spinner-rotate/`, then adds a "
        "`SessionStart` hook to `~/.claude/settings.json`. On every start, `rotate.py` picks "
        "today's category and writes it to `spinnerVerbs` (in both the CLI settings and, if "
        "present, VS Code's settings). Run `./uninstall.sh` to remove everything cleanly.\n"
    )

    # ---- Categories ----
    add("## Categories\n")
    for n in names:
        verbs = cats[n]
        add(f"### {n}\n")
        add(f"({len(verbs)} verbs)\n")
        add("| Verb |")
        add("|------|")
        for v in verbs:
            add(f"| {cell(v)} |")
        add("")
        add("<details>")
        add("<summary><strong>Copy as list</strong> (paste into <code>verbs</code>)</summary>\n")
        add("```")
        for v in verbs:
            add(f'"{v}",')
        add("```")
        add("</details>\n")

    # ---- Customizing ----
    add("## Customizing\n")
    add("Edit `categories.json` — a simple JSON object — then run the build script to refresh this README:\n")
    add("```json")
    add("{")
    add('  "My Category": ["Verb one", "Verb two"],')
    add('  "Another Category": ["First", "Second", "Third"]')
    add("}")
    add("```\n")
    add("```bash")
    add("python3 scripts/build_readme.py   # regenerates README.md and checks counts")
    add("```\n")
    add("- Categories are shown alphabetically; each day the rotation script picks one from a shuffled cycle.")
    add("- Within a cycle you never get the same category twice; the order reshuffles each cycle.")
    add("")

    # ---- Contributing / Credits / License ----
    add("## Contributing\n")
    add(
        "Have a verb or a whole theme that's missing? Open a pull request. Edit "
        "`categories.json`, run `python3 scripts/build_readme.py`, and commit both files — the "
        "counts in this README update automatically.\n"
    )

    add("## Credits\n")
    add(
        "Inspired by and built on the excellent work of [wynandw87](https://github.com/wynandw87) "
        "in [claude-code-spinner-verbs](https://github.com/wynandw87/claude-code-spinner-verbs). "
        "Many of the category themes and verb ideas trace back to that project — thank you! The "
        "curated subset, daily-rotation script, and installer are this repo's own additions.\n"
    )

    add("## License\n")
    add(
        "MIT — see [LICENSE](LICENSE). Category themes are pop-culture references used descriptively.\n"
    )

    with open(README.with_suffix("")) if False else open(README, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"Wrote README.md: {n_cats} categories, {total} verbs")


if __name__ == "__main__":
    main()
