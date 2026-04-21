#!/usr/bin/env python3
“””
Daily Reflection Tree — CLI Agent (Part B)
Loads reflection-tree.json and walks it deterministically.
No LLM calls at runtime. Pure tree traversal + state interpolation.

Usage:
python3 agent.py
python3 agent.py –tree path/to/reflection-tree.json
python3 agent.py –transcript  # save transcript to file
“””

import json
import sys
import os
import re
import time
import argparse
from datetime import datetime
from pathlib import Path
from textwrap import fill, indent

# ─── ANSI color helpers ─────────────────────────────────────────────────────

RESET  = “\033[0m”
BOLD   = “\033[1m”
DIM    = “\033[2m”
CYAN   = “\033[96m”
GREEN  = “\033[92m”
YELLOW = “\033[93m”
BLUE   = “\033[94m”
MAGENTA= “\033[95m”
WHITE  = “\033[97m”
GRAY   = “\033[37m”

def c(text, color): return f”{color}{text}{RESET}”
def bold(text): return c(text, BOLD)
def dim(text): return c(text, DIM)

COLS = 72  # wrap width

def wrap(text, prefix=””):
lines = text.split(”\n”)
out = []
for line in lines:
if line.strip() == “”:
out.append(””)
else:
out.append(fill(line, width=COLS - len(prefix)))
return (”\n” + prefix).join(out)

# ─── Tree Engine ─────────────────────────────────────────────────────────────

class ReflectionEngine:
def **init**(self, tree_path: str):
with open(tree_path, “r”) as f:
data = json.load(f)

```
    self.meta = data["meta"]
    self.nodes = {n["id"]: n for n in data["nodes"]}
    self.state = {
        "answers": {},          # node_id → chosen option value
        "axis1": {"internal": 0, "external": 0},
        "axis2": {"contribution": 0, "entitlement": 0},
        "axis3": {"self": 0, "team": 0, "altrocentric": 0},
    }
    self.transcript = []

def dominant(self, axis: str) -> str:
    counts = self.state[axis]
    if all(v == 0 for v in counts.values()):
        return "mixed"
    winner = max(counts, key=counts.get)
    # tie → "mixed"
    vals = list(counts.values())
    if vals.count(max(vals)) > 1:
        return "mixed"
    return winner

def interpolate(self, text: str) -> str:
    """Replace {NODE_ID.answer} and {axis.dominant} placeholders."""
    # Replace {NODE_ID.answer}
    def answer_sub(m):
        node_id = m.group(1)
        ans = self.state["answers"].get(node_id, "")
        if ans:
            # Find the label for this value
            node = self.nodes.get(node_id, {})
            for opt in node.get("options", []):
                if isinstance(opt, dict) and opt.get("value") == ans:
                    # Return just the text part of the label (strip emoji prefix)
                    label = opt.get("label", ans)
                    label = re.sub(r'^[^\w]*', '', label).strip()
                    return label
        return ans

    text = re.sub(r'\{([A-Z0-9_]+)\.answer\}', answer_sub, text)

    # Replace **bold** markdown
    text = re.sub(r'\*\*(.+?)\*\*', lambda m: bold(m.group(1)), text)

    return text

def apply_signal(self, signal: str):
    if not signal:
        return
    parts = signal.split(":")
    if len(parts) != 2:
        return
    axis, pole = parts
    if axis in self.state and pole in self.state[axis]:
        self.state[axis][pole] += 1

def resolve_decision(self, node: dict) -> str:
    """Return the target node ID based on routing rules."""
    for option in node["options"]:
        condition = option["condition"]
        # Parse: "NODE_ID.answer=VAL1|VAL2"
        m = re.match(r'([A-Z0-9_]+)\.answer=(.+)', condition)
        if m:
            ref_node, values_str = m.group(1), m.group(2)
            accepted = values_str.split("|")
            actual = self.state["answers"].get(ref_node, "")
            if actual in accepted:
                return option["target"]
        # Simple axis condition: "axis1.dominant=internal"
        m2 = re.match(r'(axis\d)\.dominant=(.+)', condition)
        if m2:
            axis, pole = m2.group(1), m2.group(2)
            if self.dominant(axis) == pole:
                return option["target"]
    return None  # fallback

def build_summary_text(self, template: str) -> str:
    """Build the summary node text with axis dominants and templates."""
    summary_node = self.nodes.get("SUMMARY", {})
    templates = summary_node.get("summaryTemplates", {})

    for axis_key in ["axis1", "axis2", "axis3"]:
        dom = self.dominant(axis_key)
        axis_label = {"axis1": "Axis 1", "axis2": "Axis 2", "axis3": "Axis 3"}[axis_key]

        pole_display = {
            "axis1": {"internal": "internal ✦", "external": "external", "mixed": "mixed"},
            "axis2": {"contribution": "contribution ✦", "entitlement": "entitlement", "mixed": "mixed"},
            "axis3": {"self": "self-centric", "team": "team-aware ✦", "altrocentric": "altrocentric ✦", "mixed": "mixed"},
        }

        display = pole_display.get(axis_key, {}).get(dom, dom)
        summary = templates.get(axis_key, {}).get(dom, dom)

        template = template.replace(f"{{{axis_key}.dominant}}", display)
        template = template.replace(f"{{{axis_key}.summary}}", summary)

    return template

def run(self, transcript_file=None):
    """Walk the tree from START."""
    self._print_header()
    current_id = "START"

    while current_id:
        node = self.nodes.get(current_id)
        if not node:
            print(c(f"\n[Error: node '{current_id}' not found]", YELLOW))
            break

        ntype = node["type"]

        if ntype == "start":
            self._render_start(node)
            current_id = node.get("target")

        elif ntype == "question":
            answer_value = self._render_question(node)
            self.state["answers"][current_id] = answer_value
            self.apply_signal(node.get("signal"))
            # Find the decision child or direct target
            current_id = self._next_node(node, current_id)

        elif ntype == "decision":
            current_id = self.resolve_decision(node)

        elif ntype == "reflection":
            self._render_reflection(node)
            self.apply_signal(node.get("signal"))
            current_id = node.get("target")

        elif ntype == "bridge":
            self._render_bridge(node)
            current_id = node.get("target")

        elif ntype == "summary":
            self._render_summary(node)
            current_id = node.get("target")

        elif ntype == "end":
            self._render_end(node)
            current_id = None

        else:
            print(c(f"\n[Unknown node type: {ntype}]", YELLOW))
            current_id = node.get("target")

    if transcript_file:
        self._save_transcript(transcript_file)

def _next_node(self, node: dict, current_id: str) -> str:
    """Find the decision child of a question node, or fall through to direct target."""
    # Look for a decision node whose parentId is current_id
    for nid, n in self.nodes.items():
        if n.get("parentId") == current_id and n.get("type") == "decision":
            return nid
    return node.get("target")

# ─── Rendering ────────────────────────────────────────────────────────

def _print_header(self):
    print()
    print(c("─" * COLS, BLUE))
    print(c(f"  {self.meta['title'].upper()}", CYAN + BOLD))
    print(c("─" * COLS, BLUE))
    print()

def _render_start(self, node: dict):
    text = self.interpolate(node["text"])
    print(c("  ◆  ", CYAN) + wrap(text, "     "))
    print()
    input(dim("  Press Enter to begin..."))
    print()
    self._log(node)

def _render_question(self, node: dict) -> str:
    text = self.interpolate(node["text"])
    print(c("  ┌─── Question ", BLUE) + c("─" * (COLS - 14), BLUE))
    print(c("  │  ", BLUE) + bold(wrap(text, "  │  ")))
    print(c("  │", BLUE))

    options = node["options"]
    labels = []
    for i, opt in enumerate(options):
        letter = chr(65 + i)  # A, B, C, D
        label = opt.get("label", opt.get("value", ""))
        labels.append((letter, opt["value"], label))
        print(c("  │  ", BLUE) + c(f"  {letter}. ", YELLOW) + wrap(label, "  │       "))

    print(c("  └" + "─" * (COLS - 3), BLUE))
    print()

    valid = {l[0].upper(): l[1] for l in labels}
    while True:
        raw = input(c("  Your answer (A/B/C/D): ", WHITE)).strip().upper()
        if raw in valid:
            chosen_value = valid[raw]
            chosen_label = next(l[2] for l in labels if l[0] == raw)
            print()
            print(dim(f"  → {chosen_label}"))
            print()
            time.sleep(0.3)
            self._log(node, answer=f"{raw}: {chosen_label}")
            return chosen_value
        else:
            print(c(f"  Please enter {'/'.join(valid.keys())}", YELLOW))

def _render_reflection(self, node: dict):
    text = self.interpolate(node["text"])
    print(c("  ╔" + "═" * (COLS - 3), GREEN))
    print(c("  ║  💡  REFLECTION", GREEN + BOLD))
    print(c("  ║", GREEN))
    for line in text.split("\n"):
        if line.strip():
            print(c("  ║  ", GREEN) + wrap(line, "  ║  "))
        else:
            print(c("  ║", GREEN))
    print(c("  ╚" + "═" * (COLS - 3), GREEN))
    print()
    input(dim("  Take a moment... press Enter to continue."))
    print()
    self._log(node)

def _render_bridge(self, node: dict):
    text = self.interpolate(node["text"])
    print(c("  ░░  ", MAGENTA) + c(wrap(text, "      "), MAGENTA + BOLD))
    print()
    time.sleep(0.5)
    self._log(node)

def _render_summary(self, node: dict):
    text = self.build_summary_text(node["text"])
    text = self.interpolate(text)
    print(c("  ╔" + "═" * (COLS - 3), YELLOW))
    print(c("  ║  📋  TODAY'S REFLECTION", YELLOW + BOLD))
    print(c("  ║", YELLOW))
    for line in text.split("\n"):
        if line.strip():
            print(c("  ║  ", YELLOW) + wrap(line, "  ║  "))
        else:
            print(c("  ║", YELLOW))
    print(c("  ╚" + "═" * (COLS - 3), YELLOW))
    print()
    input(dim("  Press Enter to close."))
    print()
    self._log(node)

def _render_end(self, node: dict):
    print(c("─" * COLS, BLUE))
    print(c(f"  {node['text']}", CYAN + BOLD))
    print(c("─" * COLS, BLUE))
    print()
    self._log(node)

def _log(self, node: dict, answer: str = None):
    entry = {"node_id": node["id"], "type": node["type"]}
    if answer:
        entry["answer"] = answer
    self.transcript.append(entry)

def _save_transcript(self, path: str):
    lines = []
    lines.append(f"# Reflection Transcript — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    for entry in self.transcript:
        ntype = entry["type"]
        nid = entry["node_id"]
        node = self.nodes[nid]
        if ntype == "question":
            lines.append(f"**Q [{nid}]** {self.interpolate(node['text'])}")
            lines.append(f"→ {entry.get('answer', '')}\n")
        elif ntype in ("reflection", "summary"):
            text = node["text"]
            if ntype == "summary":
                text = self.build_summary_text(text)
            lines.append(f"**{ntype.upper()} [{nid}]**\n{self.interpolate(text)}\n")
    lines.append(f"\n---\nAxis tallies: {json.dumps(self.state, indent=2)}")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(c(f"  Transcript saved to: {path}", DIM))
```

# ─── Entry point ─────────────────────────────────────────────────────────────

def main():
parser = argparse.ArgumentParser(description=“Daily Reflection Tree CLI Agent”)
parser.add_argument(”–tree”, default=“reflection-tree.json”,
help=“Path to the tree JSON file”)
parser.add_argument(”–transcript”, action=“store_true”,
help=“Save session transcript to a file”)
args = parser.parse_args()

```
tree_path = args.tree
if not os.path.exists(tree_path):
    # Try relative to this script
    script_dir = Path(__file__).parent
    tree_path = str(script_dir / "reflection-tree.json")

if not os.path.exists(tree_path):
    print(c(f"[Error] Tree file not found: {args.tree}", YELLOW))
    sys.exit(1)

transcript_path = None
if args.transcript:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_path = f"transcript_{ts}.md"

engine = ReflectionEngine(tree_path)
try:
    engine.run(transcript_file=transcript_path)
except KeyboardInterrupt:
    print(c("\n\n  Session ended early. See you tomorrow.", CYAN))
```

if **name** == “**main**”:
main()
