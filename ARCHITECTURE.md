%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#e1f5fe', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#fff'}}}%%
graph TD
    %% Main Nodes
    Node1((<b>1. OBSERVE</b><br/>Data & Signal))
    Node2[<b>2. DEFINE THE PROBLEM</b><br/>Identify gaps through]
    Node3((<b>3. FIND VALID ANSWERS</b><br/>Hypothesis & Deep))
    Node4[<b>4. DETERMINE BEST ACTION</b><br/>Decision Making & Strategy]
    Node5((<b>5. SCALE BEST ACTION</b><br/>Implementation &))
    Node6[<b>6. ACHIEVE SOLUTION</b><br/>Desired Outcome Reached]

    %% Main Flow Connections
    Node1 -->|Environmental| Node2
    Node2 -->|Inquiry & Root Cause| Node3
    Node3 -->|Insights & Evidence| Node4
    Node4 -->|Execution Planning| Node5
    Node5 -->|Operational Efficiency| Node6

    %% Sub-processes (Discovery Engine)
    subgraph "The Discovery Engine (Finding Action)"
    direction TB
    Node2 -.-> S1[Analyze]
    S1 -.-> S2[Ask 'Why' Multiple]
    S2 -.-> S3[Isolate]
    S3 -.-> Node3
    end

    %% Sub-processes (Impact Engine)
    subgraph "The Impact Engine (Leading to Solution)"
    direction TB
    Node4 -.-> E1[Pilot / Test]
    E1 -.-> E2[Measure]
    E2 -.-> E3[Standardize]
    E3 -.-> Node5
    end

    %% Feedback Loops
    Node6 -.->|Monitor results against baseline| Node1
    Node3 -.->|If answers are invalid| Node1
    Node5 -.->|If scaling| Node4

    %% Styling
    style Node1 fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    style Node3 fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    style Node5 fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    
    style Node2 fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px,color:#000
    style Node4 fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px,color:#000
    style Node6 fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px,color:#000

    style S1 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
    style S2 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
    style S3 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
    style E1 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
    style E2 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
    style E3 fill:#fff,stroke:#757575,stroke-dasharray: 5 5
