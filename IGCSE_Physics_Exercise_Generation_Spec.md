# IGCSE Physics Exercise Generation Specification

## Overview

**Role:** Expert Examiner and Exercise Creator for CAIE IGCSE Physics (0625)  
**Syllabus:** Cambridge IGCSE Physics (0625/0972)  
**Total Questions:** 100 exercises  
**Purpose:** Generate practice questions suitable for students based on learning objectives

---

## Syllabus Content Specification

The IGCSE Physics syllabus consists of **6 main topics**. Each topic contains subtopics with learning objectives classified as **Core** (for all candidates) or **Supplement** (Extended curriculum only).

### Topic Overview

| Topic | Title | Subtopics | Data Source |
|-------|-------|-----------|-------------|
| 1 | Motion, forces and energy | 1.1–1.8 | `section_1.json` |
| 2 | Thermal physics | 2.1–2.3 | `section_2.json` |
| 3 | Waves | 3.1–3.4 | `section_3.json` |
| 4 | Electricity and magnetism | 4.1–4.5 | `section_4.json` |
| 5 | Nuclear physics | 5.1–5.2 | `section_5.json` |
| 6 | Space physics | 6.1–6.2 | `section_6.json` |

### Topic 1: Motion, Forces and Energy

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 1.1 | Physical quantities and measurement techniques | 3 | 4 |
| 1.2 | Motion | 8 | 5 |
| 1.3 | Mass and weight | 4 | 1 |
| 1.4 | Density | 3 | 1 |
| 1.5 | Forces (Effects, Turning effect, Centre of gravity) | 11 | 6 |
| 1.6 | Momentum | 0 | 4 |
| 1.7 | Energy, work and power | 7 | 7 |
| 1.8 | Pressure | 3 | 1 |

### Topic 2: Thermal Physics

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 2.1 | Kinetic particle model of matter | 7 | 4 |
| 2.2 | Thermal properties and temperature | 8 | 6 |
| 2.3 | Transfer of thermal energy | 6 | 9 |

### Topic 3: Waves

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 3.1 | General properties of waves | 8 | 2 |
| 3.2 | Light (Reflection, Refraction, Lenses, Dispersion) | 14 | 8 |
| 3.3 | Electromagnetic spectrum | 5 | 5 |
| 3.4 | Sound | 9 | 3 |

### Topic 4: Electricity and Magnetism

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 4.1 | Simple phenomena of magnetism | 9 | 2 |
| 4.2 | Electrical quantities | 18 | 10 |
| 4.3 | Electric circuits | 9 | 5 |
| 4.4 | Electrical safety | 5 | 0 |
| 4.5 | Electromagnetic effects | 11 | 10 |

### Topic 5: Nuclear Physics

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 5.1 | The nuclear model of the atom | 7 | 4 |
| 5.2 | Radioactivity | 10 | 8 |

### Topic 6: Space Physics

| ID | Subtopic | Core LOs | Supplement LOs |
|----|----------|----------|----------------|
| 6.1 | The Earth and the Solar System | 9 | 5 |
| 6.2 | Stars and the Universe | 6 | 13 |

### Learning Objective Structure

Each JSON file uses the following schema:

```json
{
  "topic_X": {
    "title": "Topic Title",
    "subtopics": [
      {
        "id": "X.Y",
        "title": "Subtopic Title",
        "learning_objectives": {
          "core": ["1 Objective text [page ref]", ...],
          "supplement": ["X Objective text [page ref]", ...]
        },
        "subsections": [...]  // Optional nested structure
      }
    ]
  }
}
```

---

## Question Distribution

### By Cognitive Level (Assessment Objectives)

| Level | AO | Description | % | Count |
|-------|-----|-------------|---|-------|
| **Recall** | AO1 | Definitions, facts, basic recall | 25% | 25 |
| **Application** | AO2 | Calculations, data interpretation, applying concepts | 50% | 50 |
| **Analysis** | AO3 | Experimental design, evaluation, problem-solving | 25% | 25 |

### By Question Type

| Question Type | AO Alignment | Count | Best For |
|---------------|--------------|-------|----------|
| Multiple Choice (MCQ) | AO1, AO2 | 20 | Quick concept checks, calculations |
| True/False with Justification | AO1, AO2 | 8 | Addressing misconceptions |
| Fill-in-the-Blank | AO1 | 8 | Vocabulary, formulas, units |
| Matching | AO1 | 5 | Linking concepts, symbols, definitions |
| Labeling Diagrams | AO1, AO2 | 7 | Apparatus, circuits, ray diagrams |
| Short Answer | AO1, AO2 | 10 | Definitions, brief explanations |
| Calculations (Structured) | AO2 | 15 | Applying formulas, unit conversions |
| Data Interpretation | AO2, AO3 | 8 | Graphs, tables, experimental data |
| Diagram/Graph Drawing | AO2 | 6 | Ray diagrams, circuits, motion graphs |
| Compare & Contrast | AO2, AO3 | 5 | Similarities/differences between concepts |
| Structured Questions | AO1–AO3 | 6 | Multi-part scaffolded problems |
| Error Analysis | AO3 | 2 | Identifying experimental errors |
| **Total** | | **100** | |

---

## Physics-Specific Question Types

### Additional Recommended Types

| Question Type | Description | Best Topics |
|---------------|-------------|-------------|
| **Diagram Drawing** | Sketch ray diagrams, circuits, force diagrams, field lines | 3.2 Light, 4.1 Magnetism, 4.3 Circuits |
| **Graph Sketching** | Draw speed-time, distance-time, I-V characteristic graphs | 1.2 Motion, 4.2 Resistance |
| **Unit Conversion** | Convert between SI units (mm→m, kW→W, mins→s) | All calculation topics |
| **Equation Selection** | Given a scenario, identify which equation to use | 1.2, 1.7, 4.2 |
| **Error/Misconception Correction** | Fix a student's wrong statement or calculation | All topics |
| **Predict & Explain** | Predict outcome of experiment and justify | 2.3 Thermal, 4.5 EM effects |
| **Compare & Contrast** | Similarities/differences between concepts | Series vs Parallel, α vs β vs γ |
| **Sequencing/Ordering** | Order steps in a process (e.g., star life cycle) | 5.2 Radioactivity, 6.2 Stars |
| **Reading Instruments** | Read values from ammeter, thermometer, ruler scales | 1.1, 4.2 |
| **Sankey Diagram Analysis** | Interpret or complete energy transfer diagrams | 1.7 Energy |

---

## Bloom's Taxonomy Verbs for Physics

### Cognitive Domain Mapping

| Bloom's Level | Verbs | CAIE Equivalent | Typical Marks |
|---------------|-------|-----------------|---------------|
| **Remember** | Define, State, List, Name, Identify, Recall, Label | AO1 | 1–2 |
| **Understand** | Describe, Explain, Outline, Summarize, Compare, Distinguish | AO1/AO2 | 2–3 |
| **Apply** | Calculate, Use, Apply, Determine, Show (that), Solve | AO2 | 2–4 |
| **Analyze** | Analyze, Deduce, Interpret, Compare, Contrast, Examine | AO2/AO3 | 3–4 |
| **Evaluate** | Evaluate, Justify, Assess, Critique, Suggest, Discuss | AO3 | 3–5 |
| **Create** | Design, Plan, Construct, Propose, Predict, Derive | AO3 | 4–6 |

### Verb → Question Type Mapping

| Verb | Content Context | → Question Type |
|------|-----------------|-----------------|
| Define | Term/quantity | Fill-in-blank, Short Answer |
| State | Fact/value/law | MCQ, True/False |
| List | Multiple items | Enumeration, Matching |
| Describe | Process/method | Short Answer, Structured Q |
| Explain | Cause/effect/mechanism | Structured Q (multi-part) |
| Calculate | Numerical | Calculation, MCQ (numerical) |
| Use | Equation application | Calculation |
| Determine | From data/graph | Data Interpretation |
| Show (that) | Derivation | Structured Calculation |
| Compare | Two+ items | Compare/Contrast table |
| Deduce | From information | Structured Q, Short Answer |
| Sketch | Visual representation | Diagram/Graph Drawing |
| Predict | Outcome | Short Answer with reasoning |
| Suggest | Improvement/solution | Extended response |
| Design | Experiment | Structured Q (practical) |

---

## AI Question Type Selection Logic

### Step 1: Parse Bloom's Taxonomy Verbs

| Bloom's Level | Verbs | → Assessment Objective |
|---------------|-------|------------------------|
| Remember | Define, State, Know, List, Label, Name | AO1 (Recall) |
| Understand | Describe, Explain, Outline, Compare | AO1/AO2 |
| Apply | Calculate, Use, Determine, Apply, Show | AO2 (Application) |
| Analyze | Analyze, Deduce, Interpret, Contrast | AO2/AO3 |
| Evaluate/Create | Suggest, Evaluate, Design, Predict, Derive | AO3 (Analysis) |

### Step 2: Identify Content Type

| Content Indicator | → Detected Type |
|-------------------|-----------------|
| Contains formula/equation | Calculation |
| References diagram/apparatus | Visual |
| Lists multiple items | Comparison/Matching |
| Describes process/sequence | Procedural |
| Involves comparison | Comparative |
| References graph | Graphical |
| Involves experiment | Experimental |

### Step 3: Map to Question Type

| Command Word | Content Type | → Recommended Question Type |
|--------------|--------------|------------------------------|
| Define | Single term | Fill-in-blank, Short Answer |
| State | Fact/value | MCQ, True/False |
| Know | Concept | MCQ, Matching |
| Calculate | Formula | Calculation, MCQ (numerical) |
| Describe | Process | Short Answer, Sequencing |
| Describe | Experiment | Structured Question |
| Sketch/Draw | Visual | Diagram Drawing, Graph Sketching |
| Explain | Why/How | Structured Question, Short Answer |
| Use equation | Formula | Calculation |
| Compare | Two+ items | Compare/Contrast, Matching |
| Know (differences) | Comparison | True/False, Compare/Contrast |

### Step 4: Filter by Topic Suitability

Not all question types are suitable for every topic. Use this matrix to filter out inappropriate types:

#### Topic-Question Type Suitability Matrix

| Question Type | T1 Motion | T2 Thermal | T3 Waves | T4 Electricity | T5 Nuclear | T6 Space |
|---------------|:---------:|:----------:|:--------:|:--------------:|:----------:|:--------:|
| MCQ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| True/False | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Fill-in-Blank | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Matching | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Short Answer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Calculation** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Graph Sketching** | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Graph Interpretation** | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ |
| **Circuit Diagram** | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Ray Diagram** | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| **Force/Field Diagram** | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| **Labeling Apparatus** | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| **Sequencing/Ordering** | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |
| **Decay Equations** | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |
| **Sankey Diagram** | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Unit Conversion** | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ |
| **Compare/Contrast** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Error Analysis** | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| **Data Interpretation** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Structured Question** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

#### Subtopic-Specific Type Mapping

| Subtopic | Required Question Types | Excluded Types |
|----------|------------------------|----------------|
| 1.2 Motion | Graph Sketching, Graph Interpretation, Calculation | Circuit Diagram, Ray Diagram |
| 1.5 Forces | Force Diagram, Calculation, Labeling | Ray Diagram, Decay Equations |
| 1.7 Energy | Sankey Diagram, Calculation, Compare/Contrast | Circuit Diagram, Ray Diagram |
| 2.1 Kinetic Model | Sequencing, Short Answer, Matching | Graph Sketching, Circuit Diagram |
| 2.3 Thermal Transfer | Labeling, Compare/Contrast, Short Answer | Graph Sketching, Circuit Diagram |
| 3.2 Light | Ray Diagram, Calculation (Snell's law), Labeling | Circuit Diagram, Decay Equations |
| 4.2 Electrical Quantities | Calculation, Graph Interpretation (I-V), Circuit Diagram | Ray Diagram, Sankey Diagram |
| 4.3 Electric Circuits | Circuit Diagram, Calculation, Compare/Contrast | Ray Diagram, Sequencing |
| 5.1 Nuclear Model | Matching, Short Answer, Decay Equations | Graph Sketching, Circuit Diagram |
| 5.2 Radioactivity | Decay Equations, Sequencing, Graph Interpretation (half-life), Compare/Contrast | Circuit Diagram, Ray Diagram |
| 6.2 Stars | Sequencing (star life cycle), Matching, Short Answer | Circuit Diagram, Labeling Apparatus |

### Step 5: Apply Content Constraints

```
IF objective.type == "core":
    → Use simpler formats (MCQ, Fill-in-blank, Short Answer)
    → Limit to AO1 and basic AO2

IF objective.type == "supplement":
    → Use complex formats (Structured, Data Interpretation)
    → Include AO2 and AO3

IF objective contains "equation" or "calculate":
    → MUST include at least one calculation question
    → Include unit conversion variant

IF objective contains "experiment" or "describe...method":
    → MUST include data interpretation or structured question
    → Include error analysis variant

IF objective contains "graph" or "sketch":
    → MUST include graph drawing or interpretation question
```

### Step 6: Topic Filtering Check

```
AFTER selecting candidate question types:

1. GET topic_id from learning_objective (e.g., "1.2", "4.3")
2. LOOKUP suitability matrix for topic
3. FILTER OUT any question types marked ✗ for that topic
4. IF required type is excluded → use closest alternative:
   - Graph Sketching excluded → use Data Interpretation or Calculation
   - Circuit Diagram excluded → use Labeling or Short Answer
   - Ray Diagram excluded → use Short Answer with description
   - Decay Equations excluded → use Matching or Fill-in-blank

5. VALIDATE final selection:
   - At least 2 different question types per subtopic
   - Core objectives: ≥1 simple format (MCQ, T/F, Fill-in-blank)
   - Supplement objectives: ≥1 complex format (Structured, Calculation)
```

### Review Criteria

Before finalizing question selection, verify:

| Check | Pass Criteria |
|-------|---------------|
| **Topic Suitability** | All selected types are marked ✓ for the topic |
| **AO Balance** | Mix of AO1, AO2, AO3 appropriate to objective |
| **Format Variety** | No more than 50% of questions are same type |
| **Required Types Used** | Subtopic-specific required types are included |
| **Excluded Types Avoided** | No excluded types appear in final selection |
| **Core/Supplement Match** | Difficulty matches objective classification |

### Example Selection

| Learning Objective | Detected | Question Types Generated |
|--------------------|----------|--------------------------|
| "Define speed as distance per unit time; use v = s/t" | Define + Equation | 1× Fill-in-blank (definition), 2× Calculation MCQ |
| "Sketch and interpret distance–time graphs" | Sketch + Graph | 1× Graph Drawing, 1× Data Interpretation |
| "Describe an experiment to determine resistance" | Describe + Experiment | 1× Structured Question (3 parts) |
| "Know the difference between d.c. and a.c." | Know + Comparison | 1× Compare/Contrast, 1× True/False |

---

## General Guidelines

- Generate **100 exercise questions** distributed as specified above
- **Separate different question types by section** — do not mix multiple question types in one section
- Questions should align with the learning objectives from the JSON data files
- **Core objectives** → simpler question formats, suitable for all candidates
- **Supplement objectives** → complex formats, Extended curriculum only
- Ensure **even coverage** across all selected topics
- Include **at least one question per learning objective** where possible

---

## Diagram Generation Guidelines

### Diagram Question Types

| Type | Description | Student Task |
|------|-------------|--------------|
| **Interpretation** | Diagram provided, student analyzes | Extract data, explain phenomena, identify components |
| **Completion** | Partial diagram provided | Add rays, arrows, labels, components, field lines |
| **Drawing** | No diagram provided | Create complete diagram from description |
| **Annotation** | Diagram provided | Add labels, mark points, indicate directions |

### Standard Question Structure with Diagrams

```
[Scenario Context - 1-2 sentences describing the physical situation]

Fig. X shows [brief description of what the diagram contains].

[DIAGRAM DESCRIPTION BLOCK - see template below]

(a) [Question referencing specific diagram element] [marks]
(b) [Analysis or calculation using diagram data] [marks]
(c) [Complete/draw/label instruction] [marks]
```

### Diagram Description Template

> **IMPORTANT:** For detailed, structured diagram descriptions, refer to the comprehensive templates in `IGCSE_Physics_Diagram_Generation_Spec.md`.

Use the **Structured Prompt Template System** with:
- **7-layer structure:** Header → Canvas → Layout → Components → Connections → Labels → Annotations
- **Grid-based positioning:** Specify exact positions using grid(x, y) coordinates
- **Explicit component attributes:** Symbol, Position, Size, Orientation, Style, Fill, Label

**Quick Reference Format:**

```
---DIAGRAM: Fig. [N]---
TYPE: [Circuit | Ray | Graph | Force | Field | Apparatus | Wave | Particle]
PURPOSE: [One-line description]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: [4:3 landscape | 3:4 portrait | 16:9 wide | 1:1 square]
GRID: [columns] × [rows]

CANVAS:
  Background: pure white

LAYOUT:
  [Overall arrangement description]

COMPONENTS:
  [Component 1]
    Symbol: [description]
    Position: grid(x, y)
    Size: [dimensions]
    Label: "[text]" [position]
  
  [Component 2]
    ...

CONNECTIONS:
  [Wire/Line 1]: [Start] → [End], [style]
  ...

ANNOTATIONS:
  [Any additional markings]
---END DIAGRAM---
```

**For complete templates by diagram type, see `IGCSE_Physics_Diagram_Generation_Spec.md`:**
- Circuit Diagram Template (with IEC symbols)
- Ray Diagram Template (converging/diverging lenses)
- Graph Template (I-V characteristics, decay curves)
- Force Diagram Template (free body diagrams)
- Field Diagram Template (magnetic/electric fields)
- Apparatus Diagram Template (practical setups)

### Topic-Specific Diagram Patterns

| Topic | Diagram Pattern |
|-------|-----------------|
| **Circuit (4.2-4.3)** | "Fig. X shows a circuit containing [battery/cell], [resistor/lamp], and [ammeter/voltmeter]. The ammeter reading is [value] A. The voltmeter reading is [value] V." |
| **Ray Diagram (3.2)** | "Fig. X shows a ray of light traveling from [medium] into [medium]. The normal is shown as a dashed line. The angle of incidence is marked as i." |
| **Lens/Mirror (3.2)** | "Fig. X shows a [converging/diverging] lens. The principal axis, principal focus F, and optical centre C are marked. An object O is placed [distance] from the lens." |
| **Force Diagram (1.5)** | "Fig. X shows a [object] with forces acting on it. Force W acts vertically downward. Force R acts [direction]." |
| **Motion Graph (1.2)** | "Fig. X shows a [distance-time / speed-time / velocity-time] graph for a moving object. The section AB shows [constant speed / acceleration / rest]." |
| **Magnetic Field (4.1)** | "Fig. X shows the magnetic field pattern around a [bar magnet / current-carrying wire / solenoid]. The field lines are shown with arrows indicating direction." |
| **Wave Diagram (3.1)** | "Fig. X shows a [transverse / longitudinal] wave. The wavelength λ and amplitude A are marked." |
| **Apparatus (Practical)** | "Fig. X shows the apparatus used to investigate [phenomenon]. A [object] is connected to a [measuring device]." |
| **Decay Curve (5.2)** | "Fig. X shows a graph of [count rate / activity / number of nuclei] against time for a radioactive sample. The initial count rate is [value]." |

### AI Diagram Trigger Detection

When learning objectives contain these keywords, diagram is **REQUIRED**:

| Keyword | Diagram Type Required |
|---------|----------------------|
| "sketch", "draw" | Drawing task |
| "circuit", "component" | Circuit diagram |
| "ray diagram", "lens", "mirror", "prism" | Ray/optical diagram |
| "graph", "plot", "interpret" | Graph (with axes labeled) |
| "field lines", "magnetic field", "electric field" | Field pattern diagram |
| "apparatus", "experiment", "method" | Apparatus/setup diagram |
| "forces acting", "free body" | Force diagram |
| "wave", "wavefront" | Wave diagram |

### Diagram Necessity Criteria

**Before adding a diagram, ask: Does the diagram ADD VALUE to the question?**

| Category | Diagram? | Examples |
|----------|----------|----------|
| **REQUIRED** | YES | Circuit analysis, ray tracing, graph interpretation, field patterns |
| **ENHANCES** | OPTIONAL | Real-world scenario calculations, apparatus context |
| **UNNECESSARY** | NO | Pure definitions, unit recalls, formula statements, simple conversions |

#### Questions That Should NOT Have Diagrams

| Question Type | Examples (No Diagram Needed) |
|---------------|------------------------------|
| Definition | "Define electric current" |
| Unit recall | "State the SI unit of charge" |
| Formula recall | "State the equation relating I, Q, and t" |
| Simple calculation | "Calculate the current if Q = 60 C and t = 30 s" |
| Concept recall | "State the difference between d.c. and a.c." |
| Fill-in-blank | Vocabulary and formula completion |
| Matching | Term-definition matching |

#### Questions That SHOULD Have Diagrams

| Question Type | Examples (Diagram Required) |
|---------------|----------------------------|
| Circuit analysis | "The ammeter in Fig. 1 reads 2.5 A..." |
| Data extraction | "Using Fig. 2, determine the current at t = 5 s" |
| Practical context | "Fig. 3 shows the apparatus used to measure..." |
| Completion task | "Complete the ray diagram in Fig. 4" |
| Labeling task | "Label the components in Fig. 5" |

### Diagram Percentage Requirements

Balance diagram usage to match CAIE exam style:

| Question Type | Minimum | Maximum | Target |
|---------------|---------|---------|--------|
| MCQ | 30% | 50% | 40% |
| Calculation | 20% | 40% | 30% |
| Short Answer | 20% | 40% | 30% |
| Structured | 60% | 90% | 70% |
| Fill-in-Blank | 0% | 20% | 10% |
| True/False | 10% | 30% | 20% |
| Matching | 0% | 10% | 0% |
| **Overall** | **30%** | **50%** | **40%** |

> **Rule:** If diagram percentage exceeds the maximum, remove diagrams from questions where they are OPTIONAL (enhances but not required).

### Example: Question WITH Diagram Description

**Without diagram (poor practice):**
```
A current of 2.5 A flows through a resistor with p.d. of 10 V.
Calculate the resistance.
```

**With diagram description (CAIE standard):**
```
A student investigates the resistance of a wire.

Fig. 1 shows the circuit used.

---DIAGRAM: Fig. 1---
TYPE: Circuit
SHOWS:
• Battery (6V) with + and - terminals marked
• Variable resistor connected in series
• Fixed resistor R (the component being tested)
• Ammeter A in series with R
• Voltmeter V connected in parallel across R
LABELS INCLUDED: A, V, R, 6V
ARROWS: Current direction from + terminal through circuit
READINGS: Ammeter shows 2.5 A, Voltmeter shows 10.0 V
---END DIAGRAM---

(a) State the purpose of the variable resistor. [1]

(b) Calculate the resistance of R. [2]

(c) On Fig. 1, mark with an X the correct position for a 
    second ammeter to measure the same current. [1]
```

### Mark Allocation for Diagram Tasks

| Task Type | Typical Marks | Marking Criteria |
|-----------|---------------|------------------|
| Label 1 component | 1 | Correct label with line to component |
| Complete ray diagram | 2-3 | Correct direction, passes through focus |
| Draw circuit diagram | 2-3 | Correct symbols, correct connections |
| Plot graph points | 1-2 | Points within ½ small square |
| Draw best-fit line | 1 | Smooth curve or straight line through points |
| Add force arrows | 1-2 | Correct direction, appropriate length |
| Mark angle/point | 1 | Accurate to within tolerance |

---

## Exercise Format Categories

### 1. Selected-Response (Objective)

These focus on recognition and basic recall and are generally the most efficient to grade.

| Format | Description |
|--------|-------------|
| **Multiple Choice (MCQ)** | Choosing the best option from a set of 3–5 |
| **True/False** | Assessing the factual accuracy of a statement |
| **Matching Columns** | Connecting related items across two lists |
| **Ranking/Ordering** | Organizing items into a logical or chronological sequence |
| **Multiple Response** | Selecting all applicable answers from a provided list |

---

### 2. Supply-Response (Short-Form)

These require students to retrieve and produce brief pieces of information.

| Format | Description |
|--------|-------------|
| **Fill-in-the-Blank (Cloze)** | Inserting missing words into a sentence |
| **Sentence Completion** | Ending a partially provided statement logically |
| **Labeling** | Identifying parts of a diagram, map, or illustration |
| **Short Answer** | Providing a concise response (usually 1–3 sentences) |
| **List/Enumeration** | Naming a specific number of items or properties |

---

### 3. Structured & Constructed Response (Long-Form)

These assess higher-order thinking, organization, and the synthesis of complex information.

| Format | Description |
|--------|-------------|
| **Structured Questions** | Multi-part tasks (a, b, c) that build in complexity |
| **Data/Source Interpretation** | Analyzing graphs, tables, or primary sources |
| **Essay Questions** | Developing long-form arguments or detailed explanations |
| **Problem-Solving** | Scientific or mathematical tasks where "showing your work" is required for partial credit |

---

## MCQ Question Guidelines

> **Role:** Senior Examiner for CAIE IGCSE Physics (0625)  
> **Paper Type:** Extended paper (high-discriminatory MCQ)

### Topic & Syllabus Reference
`[INSERT TOPIC, e.g., 4.2 Electrical Quantities]`

### Task Requirements

#### The Stem
- Create a **clear, unambiguous problem statement**
- Use **international standard terminology** (e.g., "electromotive force" instead of "voltage" where appropriate)
- Ensure the scenario is **physically plausible** (values must reflect real-world physics)

#### The Options (The 4-Option Rule)

| Option | Type | Description |
|--------|------|-------------|
| **Key** | Correct Answer | The mathematically and physically accurate answer |
| **Distractor 1** | Calculation Error | Based on a common mathematical slip (e.g., forgetting a square root, or a $\frac{1}{2}$ factor) |
| **Distractor 2** | Unit/Conversion Error | Based on failing to convert units (e.g., $\text{cm}$ to $\text{m}$, $\text{mins}$ to $\text{secs}$, or $\text{kW}$ to $\text{W}$) |
| **Distractor 3** | Conceptual Misconception | Based on a fundamental physics error (e.g., confusing mass with weight, or series with parallel rules) |

### Technical Constants
- Use $g = 9.8 \text{ m/s}^2$ unless otherwise specified
- Final answers should be rounded to **2 significant figures**
- Use **LaTeX** for all scientific notation and formulas: $E = mc^2$

### Physical Constants Reference

| Constant | Symbol | Value |
|----------|--------|-------|
| Speed of light in vacuum | $c$ | $3.0 \times 10^8 \text{ m/s}$ |
| Gravitational field strength (Earth) | $g$ | $9.8 \text{ N/kg}$ |
| Speed of sound in air | — | $330\text{–}350 \text{ m/s}$ |
| Specific heat capacity of water | $c$ | $4200 \text{ J/(kg·°C)}$ |
| Specific latent heat of fusion (ice) | $L_f$ | $3.34 \times 10^5 \text{ J/kg}$ |
| Specific latent heat of vaporization (water) | $L_v$ | $2.26 \times 10^6 \text{ J/kg}$ |
| Absolute zero | — | $-273 \text{ °C}$ / $0 \text{ K}$ |
| Atmospheric pressure | — | $1.0 \times 10^5 \text{ Pa}$ |
| Density of water | $\rho$ | $1000 \text{ kg/m}^3$ |
| 1 light-year | — | $9.5 \times 10^{15} \text{ m}$ |
| Hubble constant | $H_0$ | $2.2 \times 10^{-18} \text{ /s}$ |

### Difficulty Progression (Implicit)

#### MCQ Progression Tiers

| Tier | Structure | Stem Complexity | Distractor Design |
|------|-----------|-----------------|-------------------|
| A | Single concept recognition | Direct question | Obviously wrong options |
| B | Single-step calculation | Given values, apply formula | Calculation errors |
| C | Two-step calculation | Requires unit conversion | Multi-error types |
| D | Multi-concept integration | Scenario-based | Conceptual + calculation errors |

#### Calculation Progression Tiers

| Tier | Steps | Data Given | Additional Challenge |
|------|-------|------------|---------------------|
| A | 1 | All values in correct units | None |
| B | 1–2 | Unit conversion required | Select correct formula |
| C | 2–3 | Multiple formulas needed | Intermediate values |
| D | 3+ | Extract from graph/table | Combine multiple concepts |

#### Structured Question Progression

| Part | Expected Content | Bloom's Level |
|------|------------------|---------------|
| (a) | Definition or state a fact | Remember |
| (b) | Apply formula or describe process | Apply/Understand |
| (c) | Explain reasoning or analyze data | Analyze |
| (d) | Evaluate, suggest, or predict | Evaluate/Create |

### Formatting Rules
- Arrange **numerical options in ascending order**
- Describe a **Diagram** if one is necessary for the question (e.g., a circuit diagram or a velocity-time graph)

### MCQ Output Template

```
[Description of the visual] (If any)

[Question Text]

Options:
A: [Value/Text]
B: [Value/Text]
C: [Value/Text]
D: [Value/Text]
```

---

## Structured Question Guidelines

### Paper Specification
Create questions suitable for:
- **Paper 2** (Core)
- **Paper 4** (Extended)
- **Paper 6** (Alternative to Practical)

### Assessment Objectives Mix

| AO | Focus Area |
|----|------------|
| **AO1** | Recall / Definitions |
| **AO2** | Calculations / Data interpretation |
| **AO3** | Experimental design / Variables |

### Bloom's Taxonomy Verbs
Use verbs from the Cognitive Domain Mapping (see above). Common verbs by level:

| Level | Verbs |
|-------|-------|
| Remember | `Define`, `State`, `List`, `Name`, `Label` |
| Understand | `Describe`, `Explain`, `Outline`, `Compare` |
| Apply | `Calculate`, `Use`, `Determine`, `Show (that)` |
| Analyze | `Deduce`, `Interpret`, `Contrast`, `Analyze` |
| Evaluate | `Suggest`, `Evaluate`, `Justify`, `Assess` |
| Create | `Design`, `Predict`, `Derive`, `Plan` |

### Scaffolding (Paper 4 Style)
Structure the question into sub-parts **(a, b, c)** that **increase in difficulty**

### Technical Formatting
- Provide the **Mark Allocation** `[x]` for each part
- Write the **Mark Scheme** separately, including **"Accept"** and **"Ignore"** criteria
- Use **LaTeX** for all formulas and scientific notation (e.g., $3.0 \times 10^8 \text{ m/s}$)
- Include a **description of a Diagram** that should accompany the question
- **Significant Figures:** Design the data so final answers should be rounded to **2 or 3 significant figures**

### Structured Question Output Template

#### 1. The Question
*(Numbered and formatted for a student paper)*

```
1. [Context/Scenario]

   (a) [First part - basic recall/definition] [x marks]
   
   (b) [Second part - application/calculation] [x marks]
   
   (c) [Third part - analysis/evaluation] [x marks]
```

#### 2. The Mark Scheme
*(Detailed with mark types)*

| Mark Type | Description |
|-----------|-------------|
| **M1** | Method mark |
| **A1** | Answer mark |
| **B1** | Independent mark (for definitions/statements) |

Include:
- Expected answers
- **"Accept"** alternatives
- **"Ignore"** criteria

#### 3. Common Misconceptions
A brief note on what students usually get wrong in this specific question.

---

## Worked Example Templates

### MCQ Example (Calculation Type)

```
A car accelerates uniformly from rest to 20 m/s in 8.0 s.
What is the acceleration of the car?

A: 0.40 m/s²
B: 2.5 m/s²
C: 28 m/s²
D: 160 m/s²
```

**Answer Key:**
- **Correct: B** — $a = \Delta v / \Delta t = 20/8 = 2.5 \text{ m/s}^2$
- **A (0.40)** — Distractor: divided wrong way (8/20)
- **C (28)** — Distractor: added instead of divided (20+8)
- **D (160)** — Distractor: multiplied instead (20×8)

---

### Structured Question Example

```
1. A student investigates the resistance of a wire.

   (a) Define resistance. [2]
   
   (b) The wire has length 2.0 m. A current of 0.50 A flows 
       when the p.d. is 3.0 V. Calculate the resistance. [2]
   
   (c) Explain how doubling the wire length affects 
       the resistance. [2]
```

**Mark Scheme:**

| Part | Mark | Expected Answer |
|------|------|-----------------|
| (a) | B1 | Resistance = p.d. / current OR opposition to current flow |
| (a) | B1 | Unit = ohm / Ω |
| (b) | M1 | R = V/I stated or substituted |
| (b) | A1 | R = 3.0/0.50 = 6.0 Ω |
| (c) | B1 | Resistance doubles / increases |
| (c) | B1 | Resistance is proportional to length |

**Common Misconceptions:**
- Confusing R = V/I with R = I/V
- Forgetting units in final answer
- Not recognizing proportional relationship

---

## Summary Checklist

### Question Generation
- [ ] 100 total questions generated
- [ ] Distribution matches: 25 AO1, 50 AO2, 25 AO3
- [ ] Questions separated by type into distinct sections
- [ ] Even coverage across selected learning objectives

### Question Types
- [ ] MCQs follow the 4-option distractor model (20 questions)
- [ ] Calculations include unit conversion variants (15 questions)
- [ ] Structured questions include mark schemes (6 questions)
- [ ] Diagrams/graphs included where required (13 questions)
- [ ] Physics-specific types used appropriately

### AI Selection Compliance
- [ ] Command words correctly parsed to determine AO level
- [ ] Content types correctly identified (formula, visual, experimental)
- [ ] Core objectives → simpler formats
- [ ] Supplement objectives → complex formats
- [ ] Equations/calculations → at least one calculation question
- [ ] Experiments → at least one data interpretation question

### Technical Requirements
- [ ] All formulas use LaTeX formatting
- [ ] Diagrams described where necessary
- [ ] Appropriate difficulty progression within structured questions
- [ ] Command words used correctly
- [ ] Answers rounded to correct significant figures
- [ ] Physical constants used correctly ($g = 9.8 \text{ m/s}^2$)

