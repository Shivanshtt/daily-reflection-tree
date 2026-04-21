# Write-Up: Design Rationale for the Daily Reflection Tree

## Why These Questions

The hardest constraint in this assignment was the fixed-options rule. It meant every question had to do two things simultaneously: feel like a genuine open question, and contain options that honestly cover the spectrum without steering the employee toward the “right” answer.

I spent the most time on this tension. The failure mode I kept running into was *loading* — writing options where two sound clearly virtuous and two clearly bad. That produces a survey, not a reflection. Real insight comes when the employee has to choose between two things that are both honest, both plausible, both things a reasonable person might actually say.

For the opening question on Axis 1 (weather metaphor), I chose something unusual on purpose. A direct question like “did you feel in control today?” immediately signals what “correct” looks like. The weather metaphor is more ambiguous — it captures the felt quality of the day before any psychological framing is introduced. It also does double duty: the employee’s word gets stored and echoed back in the next question, which creates the feeling of being heard.

For Axis 2, the contribution vs. entitlement axis, I was most careful about moralizing. Entitlement is invisible from the inside — if you ask “did you feel entitled today?” you’ll never surface it. So I asked instead about what occupied mental space, and about what happened when recognition didn’t come. The behavior after a slight (pulling back, letting it color the day) is a far more honest signal than any self-report about attitudes.

For Axis 3, the design challenge was that most employees don’t think about “radius of concern” at all. The opening question (“who is in the frame?”) is designed to elicit this naturally — the employee simply describes who they’re thinking about, and the tree responds to the width of that answer, not its quality.

## How the Branching Was Designed

The branching logic follows a principle I’d call **depth-first honesty**: rather than routing on the first signal, the tree waits for a second confirming signal before assigning a reflection. A single answer tells you where someone is right now; two answers on the same axis tell you something more stable.

Each axis uses a two-question structure:

- **Q1** establishes an initial orientation (high/low agency, contribution/entitlement, wide/narrow)
- **Q2** deepens specifically in the direction Q1 indicated

This means two employees who give very different Q1 answers can converge on the same reflection if Q2 reveals a shared underlying pattern — and vice versa. The tree is measuring something more nuanced than simple binaries.

**Trade-off 1: Depth vs. coverage.** I chose to go deeper on each axis (two substantive questions) rather than wider (three axes with one question each). This loses some coverage — there are patterns the tree won’t catch — but gains conversational texture. A tired employee at 7pm will feel the difference between a questionnaire and a dialogue.

**Trade-off 2: Mixed states.** I added “mixed” reflection nodes on each axis rather than forcing binary routing. This was a deliberate choice against simplification. Real human psychology on a given day is usually mixed. Forcing an internal/external binary would feel inaccurate to most people most days. The mixed reflections are the most honest responses the tree gives.

**Trade-off 3: Bridge language.** The bridges between axes aren’t neutral connectors — they’re designed to carry something forward. The Axis 1→2 bridge (“Now let’s look at what you gave”) connects agency to generosity: if you saw your own hand in the day, that same hand can reach outward. The Axis 2→3 bridge (“Let’s look at who else was in the room”) connects giving to radius: who you gave to is inseparable from how wide your circle of concern extends.

## Psychological Sources

- **Rotter (1954)**: The locus of control construct is the backbone of Axis 1. I avoided using the clinical language (“internal” / “external”) in the tree itself because it sounds like a test. The questions surface the construct without naming it.
- **Dweck (2006)**: Growth mindset is embedded in the Q2 options for Axis 1 — particularly in options that separate “I adapted” from “I got lucky.” Attribution theory (do you attribute success to effort or circumstance?) is the operational mechanism.
- **Campbell et al. (2004)**: The Psychological Entitlement Scale informed Axis 2 framing. Key subscales — deservingness, exploitation of others, resistance to constraints — shaped what I looked for in the options.
- **Organ (1988)**: OCB taxonomy (altruism, conscientiousness, civic virtue) informed the contribution-side options on Axis 2. “Helped someone with something not my job” is operationalized altruism.
- **Maslow (1969)**: The self-transcendence concept is genuinely underused. Axis 3 is built on the idea that the healthiest form of concern isn’t self-actualization but the expansion of the self to include others. The reflection language tries to convey this as expansion, not sacrifice.
- **Batson (2011)**: Perspective-taking vs. empathic concern distinction informed how I worded the Axis 3 questions — asking about *noticing* someone’s struggle (perspective-taking: cognitive) before asking about *feeling* toward them (empathic concern: affective).

## What I’d Improve With More Time

**1. Closing the loop across axes.** The summary node currently reports on each axis independently. What I’d want is cross-axis synthesis: “You saw your agency clearly today (Axis 1) but stayed inside your own frame (Axis 3). That’s a common pattern. Agency without transcendence can start to feel hollow over time.” These cross-signals would require storing not just axis tallies but the axis pairings.

**2. Longitudinal state.** A single session is a low-resolution signal. With week-over-week tracking, the tree could say “This is the third time this week you’ve leaned external on Axis 1 after describing your day as ‘storm’ or ‘fog’.” That’s when reflection becomes genuinely useful — when the pattern becomes visible.

**3. Resistance detection.** Some employees will click through as fast as possible. The tree can’t stop this, but it could be designed to surface it — a late-tree question like “How honest were you in this session?” with options that range from “Pretty honest” to “I clicked to get it done.” That self-report is itself a signal, and it closes the loop without accusation.

**4. Persona testing.** I tested this tree mentally against three personas: a high-performing individual contributor who tends to self-attribute, a middle manager who measures recognition closely, and a new joiner who is genuinely focused on learning. The tree works differently for all three, which is good. I’d want to do structured persona walkthroughs with real humans before shipping.
