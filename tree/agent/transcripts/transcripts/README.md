# Daily Reflection Tree — DT Fellowship Submission

## Structure

```
/tree/
  reflection-tree.json    ← Part A: the complete tree (47 nodes, 3 axes)
  tree-diagram.md         ← Part A: Mermaid visual diagram + node count table

/agent/
  agent.py                ← Part B: deterministic Python CLI agent

/transcripts/
  persona-1-transcript.md ← Victor / Contributing / Altrocentric path
  persona-2-transcript.md ← Victim / Entitled / Self-Centric path

write-up.md               ← Design rationale (questions, branching, sources)
README.md                 ← This file
```

-----

## Part A: Reading the Tree

The tree lives in `tree/reflection-tree.json`. It is a flat array of nodes. Every node has:

|Field     |Purpose                                                                                               |
|----------|------------------------------------------------------------------------------------------------------|
|`id`      |Unique string identifier                                                                              |
|`parentId`|Structural parent (for hierarchy; routing uses `target` fields)                                       |
|`type`    |`start`, `question`, `decision`, `reflection`, `bridge`, `summary`, `end`                             |
|`text`    |What the employee sees. `{NODE_ID.answer}` placeholders are interpolated at runtime.                  |
|`options` |For questions: array of `{value, label}`. For decisions: array of `{condition, target}` routing rules.|
|`target`  |Default next node after this one.                                                                     |
|`signal`  |`axis:pole` tag — increments the state tally when this node is traversed.                             |

### Tracing a Path (No Code Required)

1. Start at node `id: "START"`, follow `target`
1. At `question` nodes, pick an option; proceed to the decision child (the node whose `parentId` matches this question and whose `type` is `decision`)
1. At `decision` nodes, match `condition` patterns against `state.answers` to find the correct `target`
1. At `reflection`, `bridge`, and `summary` nodes, follow `target`
1. At `end`, session is complete

### Decision Condition Syntax

```
NODE_ID.answer=VALUE1|VALUE2   →  if the answer stored for NODE_ID is one of VALUE1 or VALUE2
```

Example:

```json
{ "condition": "A1_OPEN.answer=Sunny|Cloudy", "target": "A1_Q1_AGENCY_HIGH" }
```

### Signal Syntax

```
axis1:internal    →  state.axis1.internal += 1
axis2:entitlement →  state.axis2.entitlement += 1
axis3:altrocentric →  state.axis3.altrocentric += 1
```

### Interpolation Syntax

`{A1_OPEN.answer}` in a text field is replaced at runtime with the label of the employee’s chosen option for node `A1_OPEN`.

-----

## Part B: Running the Agent

**Requirements:** Python 3.7+ (no external libraries)

```bash
# Basic run
python3 agent/agent.py

# Specify tree location
python3 agent/agent.py --tree tree/reflection-tree.json

# Save transcript
python3 agent/agent.py --transcript
```

The agent:

- Loads `reflection-tree.json` from disk at runtime (not hardcoded)
- Walks nodes deterministically based on employee input
- Accumulates per-axis tallies via signals
- Interpolates employee answers into reflection/summary text
- Outputs a color-coded CLI interface
- Optionally saves a markdown transcript

**No LLM calls at runtime.** The agent is pure Python: JSON loading, dictionary lookups, string replacement, and `input()` calls.

-----

## Tree Statistics

|Metric          |Count|Requirement|
|----------------|-----|-----------|
|Total nodes     |47   |25+ ✓      |
|Question nodes  |18   |8+ ✓       |
|Decision nodes  |15   |4+ ✓       |
|Reflection nodes|9    |4+ ✓       |
|Bridge nodes    |2    |2+ ✓       |
|Axes covered    |3    |3 ✓        |
|Summary nodes   |1    |1+ ✓       |

-----

## Key Design Choices

1. **Two-question depth per axis.** Rather than one question per axis, each axis uses two substantive questions. The first establishes orientation; the second deepens in the indicated direction. This makes the tree feel like a dialogue, not a survey.
1. **Mixed-state reflections.** Every axis has an “internal/contribution/team” reflection, an “external/entitlement/self” reflection, and a “mixed” reflection. Real human days are rarely cleanly one pole or the other. The mixed path is the most common real-world path.
1. **Answer interpolation.** Reflection nodes echo the employee’s own word (“You said ‘Stormy’…”) to create the feeling of being heard. This is a deliberate UX choice — it distinguishes the tool from a generic checklist.
1. **No moralizing.** The tree never tells the employee what they *should* have done. The reflections name what was observed and offer a reframe. The “entitlement” reflection says “the ledger takes up space” — not “you were selfish.”
1. **Axes connected by bridges.** Bridge language is not neutral. The Axis 1→2 bridge connects agency to generosity; the Axis 2→3 bridge connects giving to radius. The progression is designed, not incidental.

-----

## Psychological Sources

- Rotter, J.B. (1954). *Social learning and clinical psychology.* — Locus of Control (Axis 1)
- Dweck, C. (2006). *Mindset.* — Growth vs. Fixed Mindset (Axis 1 branching)
- Campbell, W.K. et al. (2004). *Psychological entitlement.* — Entitlement construct (Axis 2)
- Organ, D.W. (1988). *Organizational citizenship behavior.* — OCB / discretionary effort (Axis 2)
- Maslow, A.H. (1969). *The farther reaches of human nature.* — Self-transcendence (Axis 3)
- Batson, C.D. (2011). *Altruism in humans.* — Perspective-taking vs. empathic concern (Axis 3)
