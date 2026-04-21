# Reflection Transcript — Persona 2: “Victim / Entitled / Self-Centric”

*Date: Example session*

-----

**START**

> Good evening. You made it through another day.
> This isn’t a performance review. There’s no right answer. This is just a quiet space to look honestly at how you showed up today — and leave knowing yourself a little better.
> Ready?

[Employee presses Enter]

-----

## AXIS 1 · LOCUS

**Q [A1_OPEN]** If today were a weather report, which best fits?

→ **C: ⛈️ Stormy — rough, and it showed**

*[Decision A1_D1: “Storm” → routes to A1_Q1_AGENCY_LOW]*

-----

**Q [A1_Q1_AGENCY_LOW]** You said “Stormy”. When things got difficult, what was your first instinct?

→ **C: Feel the weight of how unfair or messy it all was**

*Signal: axis1:external*
*[Decision A1_D3: answer=C → routes to A1_Q2_EXTERNAL]*

-----

**Q [A1_Q2_EXTERNAL]** On a tough day, where does your mind go first?

→ **A: To the people or systems that made it harder**

*Signal: axis1:external*
*[Decision A1_D7: answer=A → routes to A1_REFLECT_EXTERNAL]*

-----

💡 **REFLECTION [A1_REFLECT_EXTERNAL]**

> Rough days pull attention outward — to what others did, what went wrong, what wasn’t fair. That’s a very human response. It doesn’t mean you’re weak.
> 
> But here’s a question worth sitting with: somewhere in today, you made a call. Maybe small. Maybe invisible to others. What was it? You don’t have to answer now — just notice that it happened.

*Signal: axis1:external*
*[Routes to BRIDGE_1_2]*

-----

🔗 **BRIDGE 1→2**

> Okay. You’ve looked at how you moved through today’s events.
> Now let’s look at the other side of the same day — not what happened to you, but what you gave.

-----

## AXIS 2 · ORIENTATION

**Q [A2_OPEN]** Think of one moment today where you interacted with someone. Which of these best describes what you brought to it?

→ **D: I felt like I was taking more than I was giving**

*[Decision A2_D1: answer=D → routes to A2_Q1_ENTITLE]*

-----

**Q [A2_Q1_ENTITLE]** During today, did a moment arise where you felt your effort wasn’t recognized or rewarded fairly?

→ **B: Yes — someone else got credit I deserved**

*Signal: axis2:entitlement*
*[Decision A2_D3: answer=B → routes to A2_Q2_ENTITLE_DEEP]*

-----

**Q [A2_Q2_ENTITLE_DEEP]** When recognition didn’t come, what did you do with that feeling?

→ **D: I pulled back — gave a little less afterward**

*Signal: axis2:entitlement*
*[Decision A2_D6: answer=D → routes to A2_REFLECT_ENTITLE]*

-----

💡 **REFLECTION [A2_REFLECT_ENTITLE]**

> The feeling of deserving more — recognition, credit, fairness — is very common. And sometimes it’s legitimate.
> 
> But here’s a gentle provocation: when we’re focused on what we’re owed, we often miss the moments where we could give. Not because we’re selfish, but because the ledger takes up all the space. Tomorrow, notice one moment where you can give something and close the ledger.

*Signal: axis2:entitlement*
*[Routes to BRIDGE_2_3]*

-----

🔗 **BRIDGE 2→3**

> You’ve looked at how you navigated today, and what you gave.
> Last axis — the widest one. Let’s look at who else was in the room with you today.

-----

## AXIS 3 · RADIUS

**Q [A3_OPEN]** When you replay today in your mind right now, who is in the frame?

→ **A: Mostly me — my tasks, my challenges, my progress**

*[Decision A3_D1: answer=A → routes to A3_Q1_SELF]*

-----

**Q [A3_Q1_SELF]** When your work went well today — who benefited, beyond you?

→ **C: Honestly, I hadn’t thought about it that way**

*Signal: axis3:self*
*[Decision A3_D2: answer=C → routes to A3_Q2_SELF_DEEP]*

-----

**Q [A3_Q2_SELF_DEEP]** If someone asked you today “who are you doing this work for?” — what would have been your honest answer?

→ **A: Myself — my growth, my output, my goals**

*Signal: axis3:self*
*[Decision A3_D5: answer=A → routes to A3_REFLECT_SELF]*

-----

💡 **REFLECTION [A3_REFLECT_SELF]**

> Today was mostly about you — your load, your targets, your problems. That’s okay. Sometimes survival mode is the only mode available.
> 
> But Maslow’s final insight — the one he added late in his life — was that self-actualization alone leaves a gap. The people who report the deepest satisfaction aren’t those who reached their personal peak. They’re the ones who found a way to carry others with them. Even one person. Even briefly.

*Signal: axis3:self*
*[Routes to SUMMARY]*

-----

📋 **SUMMARY**

> Here’s what today looked like:
> 
> **On agency:** You leaned external — the day’s weight pulled your attention outward.
> 
> **On contribution:** You leaned entitlement — you noticed what you were owed.
> 
> **On radius:** You leaned self-centric — the frame was mostly your own experience.
> 
> None of this is a grade. It’s a mirror. The same mirror, offered again tomorrow.

-----

**END**

> See you tomorrow.

-----

## Axis Tallies

```json
{
  "axis1": { "internal": 0, "external": 2 },
  "axis2": { "contribution": 0, "entitlement": 2 },
  "axis3": { "self": 2, "team": 0, "altrocentric": 0 }
}
```

**Path taken:** START → A1_OPEN(Storm) → A1_Q1_AGENCY_LOW(C) → A1_Q2_EXTERNAL(A) → A1_REFLECT_EXTERNAL → BRIDGE_1_2 → A2_OPEN(D) → A2_Q1_ENTITLE(B) → A2_Q2_ENTITLE_DEEP(D) → A2_REFLECT_ENTITLE → BRIDGE_2_3 → A3_OPEN(A) → A3_Q1_SELF(C) → A3_Q2_SELF_DEEP(A) → A3_REFLECT_SELF → SUMMARY → END

-----

## How This Differs from Persona 1

|Node         |Persona 1 (Victor)                          |Persona 2 (Victim)                          |
|-------------|--------------------------------------------|--------------------------------------------|
|A1_OPEN      |Sunny                                       |Storm                                       |
|A1 Q1 branch |AGENCY_HIGH                                 |AGENCY_LOW                                  |
|A1 Q2 branch |INTERNAL                                    |EXTERNAL                                    |
|A1 reflection|“You kept your hand on the wheel”           |“Somewhere, you made a call”                |
|A2_OPEN      |“I gave something”                          |“I felt like I was taking more”             |
|A2 Q1 branch |CONTRIB                                     |ENTITLE                                     |
|A2 Q2 branch |CONTRIB_DEEP                                |ENTITLE_DEEP                                |
|A2 reflection|“You were investing”                        |“The ledger takes up space”                 |
|A3_OPEN      |“Someone outside my circle”                 |“Mostly me”                                 |
|A3 Q1 branch |WIDE                                        |SELF                                        |
|A3 Q2 branch |ALTROCENTRIC                                |SELF_DEEP                                   |
|A3 reflection|“You’re larger for including others”        |“Survival mode is okay — but notice the gap”|
|Summary      |internal ✦ / contribution ✦ / altrocentric ✦|external / entitlement / self-centric       |

The same tree, the same questions, the same code — but two completely different conversations and two completely different mirrors.
