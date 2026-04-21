flowchart TD
    START([🌙 START\nGood evening...]) --> A1_OPEN

    %% AXIS 1
    subgraph AX1["AXIS 1 · LOCUS — Victim vs Victor"]
        A1_OPEN[Q: Today as weather?\nSunny / Cloudy / Storm / Fog]
        A1_D1{Branch}
        A1_Q1_HIGH[Q: When things went well,\nwhat made it happen?]
        A1_Q1_LOW[Q: When things got hard,\nwhat was your instinct?]
        A1_D2{Branch} 
        A1_D3{Branch}
        A1_Q2_INT[Q: Something went wrong.\nYour honest first thought?]
        A1_Q2_MH[Q: When someone else\naffected your work?]
        A1_Q2_ML[Q: Did you notice a moment\nwhere you had a choice?]
        A1_Q2_EXT[Q: On a tough day,\nwhere does your mind go?]
        A1_D4{Branch}
        A1_D5{Branch}
        A1_D6{Branch}
        A1_D7{Branch}
        R_INT[💡 REFLECT: Internal\nYou kept your hand on the wheel.]
        R_MIX1[💡 REFLECT: Mixed\nYou weren't fully in or out.]
        R_EXT[💡 REFLECT: External\nTough days pull attention outward.]
    end

    A1_OPEN --> A1_D1
    A1_D1 -->|Sunny/Cloudy| A1_Q1_HIGH
    A1_D1 -->|Storm/Fog| A1_Q1_LOW
    A1_Q1_HIGH --> A1_D2
    A1_Q1_LOW --> A1_D3
    A1_D2 -->|A/C - internal| A1_Q2_INT
    A1_D2 -->|B/D - mixed| A1_Q2_MH
    A1_D3 -->|A/D - mixed| A1_Q2_ML
    A1_D3 -->|B/C - external| A1_Q2_EXT
    A1_Q2_INT --> A1_D4
    A1_Q2_MH --> A1_D5
    A1_Q2_ML --> A1_D6
    A1_Q2_EXT --> A1_D7
    A1_D4 -->|A/C| R_INT
    A1_D4 -->|B/D| R_MIX1
    A1_D5 -->|A/C| R_INT
    A1_D5 -->|B/D| R_MIX1
    A1_D6 -->|A/B| R_MIX1
    A1_D6 -->|C/D| R_EXT
    A1_D7 -->|A/C/D| R_EXT
    A1_D7 -->|B| R_MIX1

    %% BRIDGE 1→2
    R_INT --> BRIDGE12
    R_MIX1 --> BRIDGE12
    R_EXT --> BRIDGE12
    BRIDGE12[🔗 BRIDGE 1→2\nNow let's look at what you gave.]

    %% AXIS 2
    subgraph AX2["AXIS 2 · ORIENTATION — Contribution vs Entitlement"]
        A2_OPEN[Q: In one interaction today,\nwhat did you bring?]
        A2_D1{Branch}
        A2_Q1_C[Q: Did you help someone\nwithout being asked?]
        A2_Q1_E[Q: Did a moment arise where\nyour effort felt unrecognized?]
        A2_D2{Branch}
        A2_D3{Branch}
        A2_Q2_CD[Q: When you helped,\nwhat drove it?]
        A2_Q2_CL[Q: What occupied your mental\nspace today?]
        A2_Q2_ED[Q: When recognition didn't come,\nwhat did you do?]
        A2_Q2_EL[Q: Did you make someone's\nday easier?]
        A2_D4{Branch}
        A2_D5{Branch}
        A2_D6{Branch}
        A2_D7{Branch}
        R_CONTRIB[💡 REFLECT: Contribution\nYou were investing, not just working.]
        R_MIX2[💡 REFLECT: Mixed\nYou gave — and kept score a little.]
        R_ENTITLE[💡 REFLECT: Entitlement\nThe ledger can crowd out the giving.]
    end

    BRIDGE12 --> A2_OPEN
    A2_OPEN --> A2_D1
    A2_D1 -->|A/B| A2_Q1_C
    A2_D1 -->|C/D| A2_Q1_E
    A2_Q1_C --> A2_D2
    A2_Q1_E --> A2_D3
    A2_D2 -->|A/B| A2_Q2_CD
    A2_D2 -->|C/D| A2_Q2_CL
    A2_D3 -->|A/B| A2_Q2_ED
    A2_D3 -->|C/D| A2_Q2_EL
    A2_Q2_CD --> A2_D4
    A2_Q2_CL --> A2_D5
    A2_Q2_ED --> A2_D6
    A2_Q2_EL --> A2_D7
    A2_D4 -->|A/B/C| R_CONTRIB
    A2_D4 -->|D| R_MIX2
    A2_D5 -->|A/C| R_CONTRIB
    A2_D5 -->|B/D| R_MIX2
    A2_D6 -->|A/B| R_MIX2
    A2_D6 -->|C/D| R_ENTITLE
    A2_D7 -->|A/B| R_MIX2
    A2_D7 -->|C/D| R_ENTITLE

    %% BRIDGE 2→3
    R_CONTRIB --> BRIDGE23
    R_MIX2 --> BRIDGE23
    R_ENTITLE --> BRIDGE23
    BRIDGE23[🔗 BRIDGE 2→3\nLet's look at who else was in the room.]

    %% AXIS 3
    subgraph AX3["AXIS 3 · RADIUS — Self-Centric vs Altrocentric"]
        A3_OPEN[Q: Replaying today —\nwho is in the frame?]
        A3_D1{Branch}
        A3_Q1_S[Q: Who benefited from\nyour work beyond you?]
        A3_Q1_T[Q: Was a colleague's\nstruggle visible to you?]
        A3_Q1_W[Q: What made you think of\nsomeone outside your circle?]
        A3_D2{Branch}
        A3_D3{Branch}
        A3_D4{Branch}
        A3_Q2_SD[Q: Who are you\ndoing this work for?]
        A3_Q2_BO[Q: Is there someone who had\na harder day than you?]
        A3_Q2_AC[Q: When you thought of others,\nwhat did you feel?]
        A3_D5{Branch}
        A3_D6{Branch}
        A3_D7{Branch}
        R_SELF[💡 REFLECT: Self\nToday was about you — that's okay.]
        R_GROWING[💡 REFLECT: Growing\nYou saw outside yourself today.]
        R_ALTRO[💡 REFLECT: Altrocentric\nFrom 'me' to 'us'. That's a real move.]
    end

    BRIDGE23 --> A3_OPEN
    A3_OPEN --> A3_D1
    A3_D1 -->|A - self| A3_Q1_S
    A3_D1 -->|B/C - team| A3_Q1_T
    A3_D1 -->|D - wide| A3_Q1_W
    A3_Q1_S --> A3_D2
    A3_Q1_T --> A3_D3
    A3_Q1_W --> A3_D4
    A3_D2 -->|A/B/D| A3_Q2_BO
    A3_D2 -->|C| A3_Q2_SD
    A3_D3 -->|A| A3_Q2_AC
    A3_D3 -->|B/C/D| A3_Q2_BO
    A3_D4 -->|A/C| A3_Q2_AC
    A3_D4 -->|B/D| A3_Q2_BO
    A3_Q2_SD --> A3_D5
    A3_Q2_BO --> A3_D6
    A3_Q2_AC --> A3_D7
    A3_D5 -->|A/D| R_SELF
    A3_D5 -->|B/C| R_GROWING
    A3_D6 -->|A/B| R_GROWING
    A3_D6 -->|C/D| R_SELF
    A3_D7 -->|A/B/C/D| R_ALTRO

    %% CLOSE
    R_SELF --> SUMMARY
    R_GROWING --> SUMMARY
    R_ALTRO --> SUMMARY
    SUMMARY[📋 SUMMARY\nAxis tallies + interpolated reflection]
    SUMMARY --> END([👋 END\nSee you tomorrow.])

    %% Styling
    classDef start fill:#1a1a2e,color:#e0e0ff,stroke:#7c7cff
    classDef question fill:#16213e,color:#c8d8e8,stroke:#4a90d9
    classDef decision fill:#0f3460,color:#e0e0ff,stroke:#e94560,shape:diamond
    classDef reflection fill:#1b3a2d,color:#b8e8c8,stroke:#3cb371
    classDef bridge fill:#2d1b33,color:#d8c8e8,stroke:#9b59b6
    classDef summary fill:#3a2000,color:#ffe8b8,stroke:#f0a030
    classDef endpoint fill:#1a1a2e,color:#e0e0ff,stroke:#7c7cff

    class START,END endpoint
    class A1_OPEN,A1_Q1_HIGH,A1_Q1_LOW,A1_Q2_INT,A1_Q2_MH,A1_Q2_ML,A1_Q2_EXT question
    class A2_OPEN,A2_Q1_C,A2_Q1_E,A2_Q2_CD,A2_Q2_CL,A2_Q2_ED,A2_Q2_EL question
    class A3_OPEN,A3_Q1_S,A3_Q1_T,A3_Q1_W,A3_Q2_SD,A3_Q2_BO,A3_Q2_AC question
    class A1_D1,A1_D2,A1_D3,A1_D4,A1_D5,A1_D6,A1_D7 decision
    class A2_D1,A2_D2,A2_D3,A2_D4,A2_D5,A2_D6,A2_D7 decision
    class A3_D1,A3_D2,A3_D3,A3_D4,A3_D5,A3_D6,A3_D7 decision
    class R_INT,R_MIX1,R_EXT,R_CONTRIB,R_MIX2,R_ENTITLE,R_SELF,R_GROWING,R_ALTRO reflection
    class BRIDGE12,BRIDGE23 bridge
    class SUMMARY summary

