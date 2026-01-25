# IGCSE Physics Educational Graphics Specification

## Overview

**Purpose:** AI Agent comprehensive guidelines for generating educational visuals in IGCSE Physics learning modules  
**Syllabus:** Cambridge IGCSE Physics (0625/0972)  
**Audience:** Module creators, instructional designers, and AI agents generating visual content  

This specification provides detailed guidelines for creating pedagogically effective educational graphics that enhance learning and align with instructional design best practices. It complements the `IGCSE_Physics_Diagram_Generation_Spec.md` (exam-style diagrams) and supports the `IGCSE_Physics_Module_Creation_Spec.md`.

---

## Role Definition

> **Activate this role when generating educational graphics for IGCSE Physics modules.**

**Persona:** Expert IGCSE Physics Textbook Illustrator  
**Expertise:** Educational graphic design, physics visualization, instructional design, AI image generation  
**Tone:** Precise, pedagogically-focused, technically accurate  

**Your Responsibilities:**
1. Create graphics that directly support learning objectives
2. Follow Dual Coding Theory and Cognitive Load Management principles
3. Use the standard color palette and style keywords consistently
4. Apply universal exclusions to ensure clean, professional output
5. Specify exact positioning for inline module integration

**Quality Standards:**
- Every graphic must have a clear pedagogical purpose
- Visual complexity appropriate for ages 14-16
- Consistent style across all module graphics
- Accessibility requirements met (alt-text, color independence)

**Reference Documents:**
- `IGCSE_Physics_Module_Creation_Spec.md` — Inline diagram templates and module structure
- `IGCSE_Physics_Diagram_Generation_Spec.md` — Exam-style technical diagrams

---

## Core Pedagogical Principles

### Dual Coding Theory Application

> **PRINCIPLE: Every major concept requires both verbal AND visual representation**
>
> Learning is enhanced when information is presented through multiple channels (verbal + visual). Graphics should not merely decorate but actively support comprehension.

| Principle | Application |
|-----------|-------------|
| **Complementarity** | Visuals must add information not easily conveyed by text alone |
| **Coherence** | Remove decorative elements that don't support learning |
| **Contiguity** | Place graphics near related text (spatial contiguity) |
| **Segmenting** | Break complex visuals into digestible chunks |
| **Signaling** | Use visual cues to highlight key information |

### Cognitive Load Management

| Strategy | Implementation |
|----------|---------------|
| **Reduce Extraneous Load** | Remove decorative graphics, unnecessary color, complex backgrounds |
| **Manage Intrinsic Load** | Segment complex diagrams into building steps |
| **Optimize Germane Load** | Use consistent visual patterns that transfer across topics |

---

## Universal Style Standards

> **See:** `IGCSE_Physics_Module_Creation_Spec.md` → Inline Diagram Description Guidelines for module integration  
> **See:** AI Prompt Generation section below for converting specifications to AI prompts

### Standard Color Palette

| Purpose | Color | Hex Code |
|---------|-------|----------|
| Primary (blue) | Blue | #3498DB |
| Secondary (green) | Green | #27AE60 |
| Tertiary (orange) | Orange | #E67E22 |
| Highlight (red) | Red | #E74C3C |
| Background | White | #FFFFFF |
| Grid/Subtle | Light Gray | #EEEEEE |

### Universal Style Keywords

Use these keywords consistently across all educational graphics:

```
educational illustration, flat design, clean lines, minimalist diagram, pure white background, sans-serif aesthetic
```

### Universal Exclusions (ALWAYS INCLUDE)

> **CRITICAL:** Include these exclusions in every AI graphic generation prompt to ensure consistent, clean output.

```
No gradient backgrounds, No 3D effects or drop shadows, No photorealistic style, No decorative elements, No embedded text or labels, No busy or complex backgrounds
```

### Output Specifications

| Specification | Value |
|---------------|-------|
| Format | PNG |
| Minimum Resolution | 1024px on longest edge |
| Background | Pure white (#FFFFFF) |
| Line Weight | 2px standard, 3px for emphasis |

### Text Handling Strategy

> **CRITICAL:** AI image generators produce unreliable text. Always request "blank label spaces" and add text in post-processing.

**Post-processing workflow:**
1. Generate unlabeled diagram with "blank annotation spaces"
2. Export as PNG
3. Add text labels using image editor (Canva, Photoshop, GIMP)
4. Save final labeled version

## Visual Content Types

### Type 1: Conceptual Illustrations

**Purpose:** Make abstract physics concepts concrete and visual

| Use Case | Visual Type | Example |
|----------|-------------|---------|
| Abstract concepts | Analogy diagrams | Current as water flow in pipes |
| Invisible phenomena | Particle representations | Gas molecules in motion |
| Mental models | Schematic representations | Electric field lines |
| Cause-effect | Process arrows | Conduction through a solid |

#### Conceptual Illustration Template

```
---CONCEPTUAL GRAPHIC---
CONCEPT: [Physics concept being illustrated]
ANALOGY/MODEL: [Real-world analogy or scientific model used]
PURPOSE: [What understanding this graphic supports]

VISUAL ELEMENTS:
  [Element 1]: 
    Description: [What it represents]
    Position: [Location in composition]
    Style: [Visual treatment]
    
  [Element 2]:
    Description: [What it represents]
    Position: [Location in composition]
    Style: [Visual treatment]

ANNOTATIONS:
  - [Label 1]: [Text] → [Element]
  - [Label 2]: [Text] → [Element]

COLOR SCHEME:
  Primary: [Main color for key elements]
  Secondary: [Supporting color]
  Background: [Background color, preferably white or very light]

STYLE: [Clean, educational, engaging but professional]
---END CONCEPTUAL GRAPHIC---
```

#### Worked Example: Electric Current Analogy

```
---CONCEPTUAL GRAPHIC---
CONCEPT: Electric current flow in a circuit
ANALOGY/MODEL: Water flowing through pipes
PURPOSE: Help students visualize invisible electron movement using familiar water flow

VISUAL ELEMENTS:
  [Water Pump]: 
    Description: Represents the battery (energy source)
    Position: Left side of diagram
    Style: Simple pump icon with circular arrows showing flow direction
    
  [Pipe System]:
    Description: Represents the wire conductor
    Position: Connects pump to water wheel in a closed loop
    Style: Transparent pipe sections showing water particles inside
    
  [Water Wheel]:
    Description: Represents a light bulb/resistor (energy consumer)
    Position: Right side of diagram
    Style: Paddle wheel rotating from water flow
    
  [Water Particles]:
    Description: Represents electrons/charge carriers
    Position: Inside pipes, equally spaced
    Style: Small blue circles with motion arrows

ANNOTATIONS:
  - "Battery" → Water Pump
  - "Wire" → Pipe System
  - "Light bulb" → Water Wheel
  - "Electrons" → Water Particles
  - "Current = flow rate" → Arrow indicating flow direction

COLOR SCHEME:
  Primary: Blue (#3498DB) for water/electrons
  Secondary: Orange (#E67E22) for energy transfer at wheel
  Background: White (#FFFFFF)

STYLE: Clean, educational, side-by-side comparison with real circuit below
---END CONCEPTUAL GRAPHIC---
```

---

### Type 2: Process Diagrams

**Purpose:** Show step-by-step procedures, cycles, or sequences

| Process Type | Visual Format |
|--------------|---------------|
| Linear sequence | Horizontal flow with numbered steps |
| Cyclical process | Circular or loop diagram |
| Branching process | Decision tree or flowchart |
| Hierarchical | Top-down tree structure |

#### Process Diagram Template

```
---PROCESS DIAGRAM---
PROCESS: [Name of process]
TYPE: [Linear | Cyclical | Branching | Hierarchical]
STEPS: [Number of steps]

LAYOUT:
  Direction: [Left-to-right | Top-to-bottom | Circular]
  Connector Style: [Arrows | Lines | None]

STEPS:
  Step 1:
    Title: [Step name]
    Description: [Brief explanation]
    Icon/Symbol: [Visual representation]
    
  Step 2:
    Title: [Step name]
    Description: [Brief explanation]
    Icon/Symbol: [Visual representation]
    
  [Continue for all steps...]

CONNECTIONS:
  Step 1 → Step 2: [Type of arrow, label if any]
  Step 2 → Step 3: [Type of arrow, label if any]

EMPHASIS:
  - Highlight: [Key steps to emphasize]
  - De-emphasize: [Background steps if any]
---END PROCESS DIAGRAM---
```

#### Worked Example: Measuring Speed Experiment

```
---PROCESS DIAGRAM---
PROCESS: Measuring average speed using a trolley and ramp
TYPE: Linear
STEPS: 5

LAYOUT:
  Direction: Left-to-right
  Connector Style: Arrows with step numbers

STEPS:
  Step 1:
    Title: Setup
    Description: Set up ramp with ruler alongside; position light gates
    Icon/Symbol: Ramp with light gate icons
    
  Step 2:
    Title: Measure Distance
    Description: Record distance (s) between light gates in metres
    Icon/Symbol: Ruler with "s" label
    
  Step 3:
    Title: Release Trolley
    Description: Release trolley from marked position; do not push
    Icon/Symbol: Hand releasing trolley
    
  Step 4:
    Title: Record Time
    Description: Data logger records time (t) between gates
    Icon/Symbol: Timer display showing "t"
    
  Step 5:
    Title: Calculate Speed
    Description: Apply v = s/t; repeat 3 times and average
    Icon/Symbol: Calculator icon with formula

CONNECTIONS:
  Step 1 → Step 2: Arrow labeled "then"
  Step 2 → Step 3: Arrow labeled "then"
  Step 3 → Step 4: Arrow labeled "triggers"
  Step 4 → Step 5: Arrow labeled "calculate"

EMPHASIS:
  - Highlight: Steps 2 and 4 (key measurements)
  - De-emphasize: None
---END PROCESS DIAGRAM---
```

---

### Type 3: Comparison Graphics

**Purpose:** Highlight similarities and differences between concepts

| Comparison Type | Visual Format |
|-----------------|---------------|
| Two items | Side-by-side panels or T-chart |
| Multiple items | Comparison table or matrix |
| Overlap focus | Venn diagram |
| Spectrum comparison | Gradient scale |

#### Comparison Graphic Template

```
---COMPARISON GRAPHIC---
COMPARING: [Item A] vs [Item B] (vs [Item C] if applicable)
PURPOSE: [What distinction students should understand]

FORMAT: [Side-by-side | Venn | Table | Scale]

ITEM A: [Name]
  Visual: [Representative image or symbol]
  Key Features:
    - [Feature 1]
    - [Feature 2]
    - [Feature 3]

ITEM B: [Name]
  Visual: [Representative image or symbol]
  Key Features:
    - [Feature 1]
    - [Feature 2]
    - [Feature 3]

SIMILARITIES (if Venn):
  - [Shared feature 1]
  - [Shared feature 2]

VISUAL DIFFERENTIATION:
  - Item A color: [Color code]
  - Item B color: [Color code]
  - Use [icons | symbols | shapes] to distinguish
---END COMPARISON GRAPHIC---
```

#### Worked Example: Speed vs Velocity

```
---COMPARISON GRAPHIC---
COMPARING: Speed vs Velocity
PURPOSE: Help students understand the key difference between scalar and vector quantities

FORMAT: Side-by-side panels with shared center

ITEM A: Speed
  Visual: Speedometer showing 50 km/h
  Key Features:
    - Scalar quantity (magnitude only)
    - Always positive
    - "How fast" an object moves
    - Unit: m/s or km/h

ITEM B: Velocity
  Visual: Arrow showing 50 km/h NORTH
  Key Features:
    - Vector quantity (magnitude + direction)
    - Can be positive or negative
    - "How fast and in which direction"
    - Unit: m/s or km/h with direction

SIMILARITIES:
  - Same numerical value possible
  - Both measure motion
  - Same SI unit (m/s)

VISUAL DIFFERENTIATION:
  - Speed color: #3498DB (blue)
  - Velocity color: #27AE60 (green)
  - Speed: circular gauge icon
  - Velocity: arrow with compass direction
---END COMPARISON GRAPHIC---
```

---

### Type 4: Annotated Photographs/Realistic Images

**Purpose:** Connect physics concepts to real-world applications

| Use Case | Image Requirements |
|----------|--------------------|
| Laboratory equipment | Clear photograph with labeled parts |
| Real-world applications | Photo with physics concepts overlaid |
| Natural phenomena | Image with explanatory annotations |
| Technology examples | Device with internal workings revealed |

#### Annotated Image Template

```
---ANNOTATED IMAGE---
SUBJECT: [What the image shows]
CONTEXT: [Real-world application or scenario]
PURPOSE: [Learning objective this supports]

BASE IMAGE:
  Description: [Detailed description of needed photograph]
  Lighting: [Bright, clear, professional]
  Angle: [Best perspective for learning]
  Focus: [Key elements that must be sharp]

ANNOTATIONS:
  [Part A]:
    Location: [Where on image]
    Label: "[Text label]"
    Leader Line: [Style of line connecting label to part]
    
  [Part B]:
    Location: [Where on image]
    Label: "[Text label]"
    Leader Line: [Style]

OVERLAYS (if applicable):
  - [Physics concept overlay, e.g., force arrows]
  - [Motion path indicators]
  - [Energy flow indicators]

CAPTION: "[Brief educational caption]"
---END ANNOTATED IMAGE---
```

---

### Type 5: Data Visualization Graphics

**Purpose:** Present scientific data, relationships, and patterns

| Data Type | Visualization |
|-----------|---------------|
| Relationships | Line graphs, scatter plots |
| Comparisons | Bar charts |
| Proportions | Pie charts (use sparingly) |
| Distributions | Histograms |
| Multi-variable | Tables with visual indicators |

#### Data Visualization Template

```
---DATA VISUALIZATION---
DATA TYPE: [What data is being shown]
GRAPH TYPE: [Line | Bar | Scatter | Table | Other]
PURPOSE: [What pattern or relationship to highlight]

AXES (if applicable):
  X-Axis:
    Label: "[Quantity] / [unit]"
    Range: [min] to [max]
    Intervals: [spacing]
    
  Y-Axis:
    Label: "[Quantity] / [unit]"
    Range: [min] to [max]
    Intervals: [spacing]

DATA REPRESENTATION:
  Data Set 1:
    Name: [Label]
    Color: [Color]
    Symbol: [Point marker style]
    Line Style: [Solid | Dashed | None]
    
  Data Set 2 (if applicable):
    Name: [Label]
    Color: [Different color]
    Symbol: [Different marker]
    Line Style: [Style]

ANNOTATIONS:
  - Key Point 1: [Description] at (x, y)
  - Key Point 2: [Description] at (x, y)

LEGEND: [Position and contents]
GRID: [Light gray, unobtrusive]
---END DATA VISUALIZATION---
```

---

### Type 6: Equation/Formula Graphics

**Purpose:** Present equations with visual context and variable definitions

| Format | Use Case |
|--------|----------|
| Annotated equation | New formula introduction |
| Variable breakdown | Complex equations with many terms |
| Unit analysis | Showing dimensional consistency |
| Equation comparison | Showing related formulas |

#### Equation Graphic Template

```
---EQUATION GRAPHIC---
EQUATION: [LaTeX or plain text formula]
NAME: [Common name for equation]
PURPOSE: [What physics relationship it describes]

EQUATION DISPLAY:
  Format: Centered, large, clear typography
  Style: [Boxed | Highlighted | Plain]
  Numbering: [e.g., Eq. 2.1]

VARIABLE ANNOTATIONS:
  [Symbol 1]:
    Name: [Full name]
    Unit: [SI unit]
    Annotation Position: [Above | Below | Side]
    
  [Symbol 2]:
    Name: [Full name]
    Unit: [SI unit]
    Annotation Position: [Position]

VISUAL CONTEXT (optional):
  - Diagram showing physical meaning of variables
  - Triangle diagram for rearrangement
  - Unit analysis display

EXAMPLE CALLOUT (optional):
  Problem: [Brief example]
  Substitution: [Values inserted]
  Answer: [Result with units]
---END EQUATION GRAPHIC---
```

#### Worked Example: Speed Equation Introduction

```
---EQUATION GRAPHIC---
EQUATION: v = s / t
NAME: Speed Equation
PURPOSE: Calculate average speed from distance and time measurements

EQUATION DISPLAY:
  Format: Large central equation with extending annotation lines
  Style: Boxed with light blue background
  Numbering: Eq. 2.1

VARIABLE ANNOTATIONS:
  [v]:
    Name: speed (or average speed)
    Unit: metres per second (m/s)
    Annotation Position: Above, with upward line
    
  [s]:
    Name: distance travelled
    Unit: metres (m)
    Annotation Position: Above right, with diagonal line
    
  [t]:
    Name: time taken
    Unit: seconds (s)
    Annotation Position: Below right, with diagonal line

VISUAL CONTEXT:
  - Formula triangle diagram below main equation
  - Triangle shows: s at top, v and t at bottom corners
  - Caption: "Cover the quantity you want to find"

EXAMPLE CALLOUT:
  Problem: A car travels 150 m in 10 s. What is its speed?
  Substitution: v = 150 m ÷ 10 s
  Answer: v = 15 m/s
---END EQUATION GRAPHIC---
```

#### Worked Example: Formula Triangle (NEW STRUCTURED FORMAT)

> **Use this template for all formula triangles.** It follows the six-layer structure for consistent AI generation.

```
---GRAPHIC: Fig. [M.N] - [Equation Name] Formula Triangle---
TYPE: Equation
PURPOSE: Help students remember and rearrange [equation, e.g., v = s/t]

CANVAS:
  Background: pure white (#FFFFFF)
  Aspect Ratio: 1:1 square
  Margins: 10% all sides

LAYOUT:
  Pattern: centered triangle with internal divisions
  Main Element: equilateral triangle, 80% of canvas width
  Divisions: horizontal divider + vertical divider in lower section

ELEMENTS:
  [Triangle Outline]
    Description: Equilateral triangle outline
    Position: center
    Size: 80% of canvas width
    Shape: equilateral triangle
    Style: solid thick (3px)
    Fill: none
    Color: black (#000000)

  [Horizontal Divider]
    Description: Line separating apex (top) from bottom sections
    Position: horizontal, middle of triangle height
    Size: spans full width of triangle at that height
    Shape: line
    Style: solid medium (2px)
    Color: black (#000000)

  [Vertical Divider]
    Description: Line separating bottom-left from bottom-right compartments
    Position: vertical, center of lower half (from horizontal divider to base)
    Size: from horizontal divider to triangle base
    Shape: line
    Style: solid medium (2px)
    Color: black (#000000)

  [Apex Variable Space]
    Description: Blank area for numerator variable
    Position: apex section (above horizontal divider)
    Size: fills upper section
    Fill: none (blank for post-processing label)

  [Bottom-Left Variable Space]
    Description: Blank area for first denominator variable
    Position: bottom-left compartment
    Size: fills bottom-left section
    Fill: none (blank for post-processing label)

  [Bottom-Right Variable Space]
    Description: Blank area for second denominator or related variable
    Position: bottom-right compartment
    Size: fills bottom-right section
    Fill: none (blank for post-processing label)

LABELS: (add in post-processing using image editor)
  - "[Numerator variable, e.g., s]" → center of apex section
  - "[Variable 1, e.g., v]" → center of bottom-left compartment
  - "[Variable 2, e.g., t]" → center of bottom-right compartment

STYLE:
  Keywords: educational illustration, flat design, minimalist, clean lines, formula triangle
  Background: pure white (#FFFFFF)
  Line Color: black (#000000)
  Label Color: blue (#3498DB) recommended for post-processing

EXCLUSIONS:
  No gradients, No shadows, No 3D effects, No embedded AI-generated text,
  No additional boxes or elements outside triangle, No circular backgrounds around variables,
  No decorative elements, No paper texture
---END GRAPHIC---
```

#### Formula Triangle: Speed (v = s/t) — Complete Example

```
---GRAPHIC: Fig. 2.1 - Speed Formula Triangle---
TYPE: Equation
PURPOSE: Help students remember and rearrange the speed equation v = s/t

CANVAS:
  Background: pure white (#FFFFFF)
  Aspect Ratio: 1:1 square
  Margins: 10% all sides

LAYOUT:
  Pattern: centered triangle with internal divisions
  Main Element: equilateral triangle, 80% of canvas width
  Divisions: horizontal divider + vertical divider in lower section

ELEMENTS:
  [Triangle Outline]
    Description: Equilateral triangle outline
    Position: center
    Size: 80% of canvas width
    Shape: equilateral triangle
    Style: solid thick (3px)
    Fill: none
    Color: black (#000000)

  [Horizontal Divider]
    Description: Line separating s (distance) from v and t
    Position: horizontal, middle of triangle height
    Size: spans full width of triangle at that height
    Shape: line
    Style: solid medium (2px)
    Color: black (#000000)

  [Vertical Divider]
    Description: Line separating v (speed) from t (time)
    Position: vertical, center of lower half
    Size: from horizontal divider to triangle base
    Shape: line
    Style: solid medium (2px)
    Color: black (#000000)

  [Distance Space (s)]
    Description: Blank area for distance variable
    Position: apex section
    Fill: none

  [Speed Space (v)]
    Description: Blank area for speed variable
    Position: bottom-left compartment
    Fill: none

  [Time Space (t)]
    Description: Blank area for time variable
    Position: bottom-right compartment
    Fill: none

LABELS: (add in post-processing)
  - "s" → center of apex section
  - "v" → center of bottom-left compartment
  - "t" → center of bottom-right compartment

STYLE:
  Keywords: educational illustration, flat design, minimalist, clean lines
  Background: pure white (#FFFFFF)
  Line Color: black (#000000)
  Label Color: blue (#3498DB)

EXCLUSIONS:
  No gradients, No shadows, No 3D effects, No embedded text,
  No extra boxes, No circular variable backgrounds
---END GRAPHIC---
```

#### Type 6 Common Errors to Avoid

| Error | Problem | Solution |
|-------|---------|----------|
| ❌ Missing vertical divider | Bottom section not split into v and t compartments | Explicitly specify "[Vertical Divider]" element |
| ❌ Extra boxes outside triangle | AI adds equation boxes or labels below triangle | Add to EXCLUSIONS: "No additional boxes outside triangle" |
| ❌ Circular backgrounds around variables | AI places variables in circles | Add to EXCLUSIONS: "No circular backgrounds around variables" |
| ❌ Embedded AI text | Letters look distorted or incorrect | Request blank spaces, add labels in post-processing |
| ❌ Unequal compartments | Bottom sections not evenly divided | Specify vertical divider at "center of lower half" |
| ❌ Triangle not centered | Composition is off-balance | Specify "Position: center" and "80% of canvas width" |
| ❌ Variables in wrong positions | Numerator not at top | Remember: numerator (product) at apex, factors at bottom |

---

### Type 7: Infographics

**Purpose:** Summarize multiple related facts or concepts in an engaging format

| Type | Best For |
|------|----------|
| Timeline | Historical developments, sequences |
| Statistical | Key numbers and facts |
| Comparative | Contrasting items or scenarios |
| Process | Step-by-step with context |
| Hierarchical | Categories and subcategories |

#### Infographic Template

```
---INFOGRAPHIC---
TOPIC: [Subject of infographic]
TYPE: [Timeline | Statistical | Comparative | Process | Hierarchical]
PURPOSE: [Summary goal]

TITLE: [Engaging, clear heading]

LAYOUT:
  Orientation: [Portrait | Landscape | Square]
  Sections: [Number and names of sections]

CONTENT BLOCKS:
  Block 1:
    Title: [Section heading]
    Key Fact: [Main information]
    Visual: [Icon or small illustration]
    
  Block 2:
    Title: [Section heading]
    Key Fact: [Main information]
    Visual: [Icon or small illustration]
    
  [Continue for all blocks...]

VISUAL STYLE:
  Color Palette: [2-3 colors maximum]
  Icon Style: [Flat | Line | Filled]
  Typography: [Clear, hierarchical headings]

FOOTER: [Source attribution or module reference]
---END INFOGRAPHIC---
```

---

### Type 8: Interactive Prompt Graphics

**Purpose:** Graphics designed for student interaction (drawing, completing, labeling)

| Interaction Type | Graphic Design |
|------------------|----------------|
| Label completion | Diagram with blank labels and leader lines |
| Draw completion | Partial diagram for student completion |
| Data reading | Graph with reading task requirements |
| Matching | Images to be connected to descriptions |

#### Interactive Graphic Template

```
---INTERACTIVE GRAPHIC---
TYPE: [Label | Draw | Read | Match | Complete]
LEARNING OBJECTIVE: [What skill this develops]
DIFFICULTY: [Basic | Intermediate | Advanced]

BASE GRAPHIC:
  Description: [What is provided to students]
  Completeness: [e.g., 60% complete, student adds rest]

STUDENT TASK:
  Instructions: "[Clear instructions for student]"
  
  Tasks:
    Task 1: [What to label/draw/complete]
    Task 2: [What to label/draw/complete]
    [Continue...]

BLANK SPACES:
  Space 1:
    Location: [Position on graphic]
    Expected Answer: [Correct response]
    
  Space 2:
    Location: [Position on graphic]
    Expected Answer: [Correct response]

ANSWER KEY:
  [Complete version of graphic or answers listed]
---END INTERACTIVE GRAPHIC---
```

---

### Type 9: Concept Maps

**Purpose:** Visualize relationships and connections between physics concepts

| Map Type | Best For |
|----------|----------|
| Hierarchical | Topic → subtopics → details |
| Network/Web | Interconnected concepts with multiple relationships |
| Flow map | Cause-effect chains |
| System map | Components and their interactions |

#### Concept Map Template

```
---CONCEPT MAP---
TOPIC: [Central concept or topic area]
SCOPE: [What learning objectives this covers]
TYPE: [Hierarchical | Network | Flow | System]

CENTRAL NODE:
  Label: [Main concept name]
  Style: Large, bold, distinct color background
  Position: Center of diagram

PRIMARY NODES: (directly connected to central node)
  Node 1:
    Label: [Concept name]
    Connection to Central: [Relationship phrase, e.g., "is measured by"]
    Arrow Direction: [Central → Node | Node → Central | Bidirectional]
    
  Node 2:
    Label: [Concept name]
    Connection to Central: [Relationship phrase]
    Arrow Direction: [Direction]

SECONDARY NODES: (connected to primary nodes)
  Node 1a:
    Label: [Concept name]
    Connected To: Node 1
    Relationship: [Linking phrase]
    
  Node 1b:
    Label: [Concept name]
    Connected To: Node 1
    Relationship: [Linking phrase]

CROSS-LINKS: (connections between non-adjacent nodes)
  Link 1: Node 1a ↔ Node 2 via [relationship phrase]

VISUAL HIERARCHY:
  - Central node: Largest, primary color
  - Primary nodes: Medium size, secondary color
  - Secondary nodes: Smaller, tertiary color
  - Cross-links: Dashed lines

KEY/LEGEND:
  - [Color 1]: [Category]
  - [Color 2]: [Category]
---END CONCEPT MAP---
```

#### Worked Example: Motion Concept Map

```
---CONCEPT MAP---
TOPIC: Motion in Physics
SCOPE: Section 2.1 - Speed, Velocity, and Acceleration
TYPE: Hierarchical with cross-links

CENTRAL NODE:
  Label: MOTION
  Style: Large oval, blue background (#3498DB), white text
  Position: Center of diagram

PRIMARY NODES:
  Node 1:
    Label: Speed
    Connection to Central: "is described by"
    Arrow Direction: Central → Node
    
  Node 2:
    Label: Velocity
    Connection to Central: "is described by"
    Arrow Direction: Central → Node
    
  Node 3:
    Label: Acceleration
    Connection to Central: "changes are described by"
    Arrow Direction: Central → Node

SECONDARY NODES:
  Node 1a:
    Label: Distance
    Connected To: Speed
    Relationship: "uses"
    
  Node 1b:
    Label: Time
    Connected To: Speed
    Relationship: "uses"
    
  Node 2a:
    Label: Displacement
    Connected To: Velocity
    Relationship: "uses"
    
  Node 3a:
    Label: Change in Velocity
    Connected To: Acceleration
    Relationship: "measures"

CROSS-LINKS:
  Link 1: Time (Node 1b) ↔ Acceleration via "is a factor in calculating"
  Link 2: Distance ↔ Displacement via "related but different"

VISUAL HIERARCHY:
  - Central node: Largest, #3498DB blue
  - Primary nodes: Medium size, #85C1E9 light blue
  - Secondary nodes: Smaller, #EEEEEE light gray
  - Cross-links: Dashed orange (#E67E22) lines

KEY/LEGEND:
  - Blue: Main concepts
  - Light blue: Subconcepts
  - Dashed orange: Cross-relationships

STYLE:
  Keywords: educational illustration, flat design, concept map
  Background: pure white (#FFFFFF)
  
EXCLUSIONS:
  No gradient backgrounds, No 3D effects, No embedded text

ASPECT RATIO: 4:3 landscape
OUTPUT: PNG, 1024px
---END CONCEPT MAP---
```

---

## AI Prompt Generation

> **Purpose:** Convert graphic specification templates into effective AI image generation prompts

### Prompt Structure Formula

```
[GRAPHIC TYPE] + [SUBJECT] + [STYLE KEYWORDS] + [COMPOSITION] + [COLOR PALETTE] + [EXCLUSIONS]
```

### AI Prompt Keywords

Use these keywords consistently across all educational graphics:

| Category | Keywords |
|----------|----------|
| **Style** | "Educational illustration", "flat design", "minimalist diagram" |
| **Aesthetic** | "Clean lines", "hand-drawn textbook style", "technical drawing" |
| **Background** | "Pure white background", "light gray background" |
| **Typography** | "Sans-serif labels" (note: add text separately for best results) |

### Text Handling Strategy

> **CRITICAL:** AI image generators produce unreliable text. Follow this strategy:

| Approach | When to Use |
|----------|-------------|
| **Generate unlabeled** | Request "blank label spaces" or "unlabeled diagram" |
| **Post-process** | Add text using image editor (Canva, Photoshop, GIMP) |
| **Overlay** | Add text via HTML/CSS in final presentation |
| **Annotation tools** | Use LMS built-in annotation features |

**In prompts, say:** "with blank annotation spaces for adding labels later"

### Universal Exclusions for AI Prompts

Add to ALL prompts to prevent common AI errors:

```
EXCLUDE:
- "No gradient backgrounds"
- "No 3D effects or drop shadows"  
- "No photorealistic style"
- "No decorative elements"
- "No embedded text or labels" (add separately)
- "No busy or complex backgrounds"
- "No perpendicular symbol (⊥) for division"
```

### AI Prompt Output Specifications

Include in prompts for consistent quality:

| Specification | Value |
|---------------|-------|
| **Aspect Ratio** | 4:3 (diagrams), 16:9 (process), 3:4 (infographics) |
| **Resolution** | Minimum 1024px on longest edge |
| **Format** | PNG (preferred), transparent background if applicable |

### Example Prompt Transformations

#### Example 1: Speed Equation (Type 6)

**Template Specification:**
```
EQUATION: v = s / t
NAME: Speed Equation
STYLE: Boxed with light blue background
VISUAL CONTEXT: Formula triangle below
```

**Effective AI Prompt:**
```
Educational physics diagram showing the speed equation. Display a 
large boxed equation with v = s/t as a properly stacked fraction, 
s above t with horizontal divider line. Light blue (#E8F4FC) 
rectangular background for equation box. Three colored annotation 
arrows: blue arrow pointing to v, green arrow to s, orange arrow 
to t, each with blank label space. Below the equation box, draw 
a formula triangle with s at top, v at bottom-left, t at bottom-right, 
separated by dashed lines. To the right of triangle, show three 
rearranged equations in colored boxes. Clean flat design, white 
background, educational illustration style, no shadows, no gradients, 
no embedded text, sans-serif aesthetic.
```

---

#### Example 2: Speed vs Velocity Comparison (Type 3)

**Template Specification:**
```
COMPARING: Speed vs Velocity
FORMAT: Side-by-side panels
ITEM A: Speedometer showing 50
ITEM B: Arrow with direction
```

**Effective AI Prompt:**
```
Educational comparison diagram with two side-by-side panels. LEFT 
panel: circular speedometer gauge showing 50, blue border (#3498DB), 
label space for "SCALAR". RIGHT panel: horizontal arrow pointing 
right with small compass rose, green border (#27AE60), label space 
for "VECTOR". Center section with connecting element between panels. 
Clean minimalist style, white background, flat design, no gradients, 
no shadows, blank spaces for adding text labels later, educational 
physics illustration.
```

---

#### Example 3: Distance vs Displacement (Type 3)

**Template Specification:**
```
COMPARING: Distance vs Displacement
SCENARIO: Person walks 4m east, then 3m north
```

**Effective AI Prompt:**
```
Educational physics diagram showing a right-angled path on a simple 
grid. Person icon at bottom-left "START" position. Blue solid arrow 
going 4 units right (east), then 3 units up (north) to "END" position. 
Separate green dashed arrow diagonal from START directly to END 
(the displacement). Right-angle symbol at corner. Two annotation 
boxes with blank spaces: one blue for "Distance = 7m", one green for 
"Displacement = 5m". Clean flat educational style, white background, 
no gradients, no shadows, minimal decorative elements, blank label 
spaces for adding text.
```

---

#### Example 4: Concept Map (Type 9)

**Template Specification:**
```
TOPIC: Motion in Physics
TYPE: Hierarchical with cross-links
CENTRAL NODE: MOTION
PRIMARY NODES: Speed, Velocity, Acceleration
```

**Effective AI Prompt:**
```
Educational concept map diagram. Large central oval labeled "MOTION" 
in blue (#3498DB). Three medium ovals branching out: "SPEED" (left), 
"VELOCITY" (center-right), "ACCELERATION" (right), all in light blue 
(#85C1E9). Solid arrows from center to each primary node. Smaller 
nodes branching from primary nodes: under Speed show "Distance" and 
"Time"; under Velocity show "Displacement" and "Direction". Dashed 
orange line connecting Speed and Velocity showing relationship. 
Clean hierarchical layout, white background, educational illustration 
style, no shadows, no gradients, blank label spaces for relationship 
text, minimalist design.
```

### AI Prompt Quality Checklist

Before generating, verify your prompt includes:

- [ ] Clear subject description
- [ ] Style keywords (flat, minimalist, educational)
- [ ] Color specifications with hex codes
- [ ] Composition/layout description
- [ ] Aspect ratio or dimensions
- [ ] "White background" or specific background
- [ ] Exclusions (no gradients, no shadows, no text)
- [ ] "Blank label spaces" if labels needed

### Common AI Prompt Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| "v = s/t equation" | AI shows s twice or misplaces | "stacked fraction with s ABOVE t" |
| Requesting text labels | AI produces illegible text | "blank label spaces for adding later" |
| No exclusions | AI adds unwanted effects | Always include "no shadows, no gradients" |
| Vague composition | Unpredictable layout | Describe exact positions: left, right, above, below |
| No color codes | Inconsistent colors | Use hex codes (#3498DB) |

### Iterative Refinement Process

1. **Generate first version** with complete prompt
2. **Evaluate output** against template specification  
3. **Identify issues** (wrong layout, missing elements, unwanted effects)
4. **Refine prompt** - add specificity where issues occurred
5. **Regenerate** and compare
6. **Post-process** - add text labels in image editor

### Tool-Specific Tips

#### For DALL-E 3 (ChatGPT)
- Use conversational descriptions
- Works well with paragraph-based prompts
- Can ask for tweaks in follow-up messages

#### For Midjourney
- Use `--ar 4:3` for aspect ratio
- Use `--no gradient shadow 3D` for exclusions
- Shorter, high-signal phrases work well

#### For Gemini / Ideogram / Other Tools
- Focus on composition description
- Be very explicit about text avoiding: "no text, no letters, no words"
- Describe element positions precisely

---

## Structured Description System

> **CRITICAL:** Use this structured format for ALL educational graphic descriptions to ensure AI generates consistent, accurate graphics.

### Six-Layer Description Structure

Describe graphics in this EXACT order to ensure consistency:

| Layer | Purpose | Required? |
|-------|---------|-----------|
| 1. **HEADER** | Type, purpose, figure number | ✓ Always |
| 2. **CANVAS** | Background, aspect ratio, margins | ✓ Always |
| 3. **LAYOUT** | Overall arrangement pattern | ✓ Always |
| 4. **ELEMENTS** | Each visual element with full attributes | ✓ Always |
| 5. **LABELS** | Text to add in post-processing | ✓ Always |
| 6. **STYLE** | Colors, keywords, exclusions | ✓ Always |

### Standard Delimiter Format

Use these delimiters for all graphic descriptions:

```
---GRAPHIC: Fig. [M.N] - [Title]---
TYPE: [Equation | Comparison | Process | Diagram | Data | Annotated | Infographic | Timeline | Concept Map]
PURPOSE: [One-line learning objective supported]

CANVAS:
  [Canvas specifications]

LAYOUT:
  [Layout pattern]

ELEMENTS:
  [Element specifications]

LABELS:
  [Post-processing labels]

STYLE:
  [Style specifications]

EXCLUSIONS:
  [What to avoid]
---END GRAPHIC---
```

---

## Zone-Based Positioning

Use zone descriptors for precise element placement (simpler than grid coordinates for educational graphics):

### Standard Nine-Zone Grid

```
┌─────────────┬─────────────┬─────────────┐
│  top-left   │  top-center │  top-right  │
├─────────────┼─────────────┼─────────────┤
│ center-left │   center    │center-right │
├─────────────┼─────────────┼─────────────┤
│ bottom-left │bottom-center│bottom-right │
└─────────────┴─────────────┴─────────────┘
```

### Triangle-Specific Zones

For formula triangles and triangular graphics:

```
           ┌───────────┐
          ╱    apex     ╲
         ╱   (top)       ╲
        ├─────────────────┤  ← horizontal divider
       ╱ bottom-  │ bottom- ╲
      ╱   left    │  right   ╲
     └────────────┴───────────┘
            ↑
     vertical divider
```

### Comparison Zones

For side-by-side comparison graphics:

```
┌──────────────┬───┬──────────────┐
│              │   │              │
│  left-panel  │ VS│ right-panel  │
│              │   │              │
└──────────────┴───┴──────────────┘
```

---

## Element Attribute Format

For EACH element in ELEMENTS section, specify ALL applicable attributes:

```
[Element Name]
  Description: [what this element represents]
  Position: [zone from positioning system above]
  Size: [small | medium | large] or [percentage, e.g., "80% of canvas width"]
  Shape: [rectangle | triangle | circle | line | arrow | custom description]
  Style: [solid | dashed | dotted] [thin (1px) | medium (2px) | thick (3px)]
  Fill: [none | solid-black | color-fill(#hexcode)]
  Color: [#hexcode] or "black (#000000)"
  Orientation: [horizontal | vertical | diagonal | angled at X°]
```

### Attribute Quick Reference

| Attribute | Options |
|-----------|---------|
| **Size** | `small` (20-30%), `medium` (40-60%), `large` (70-90%) |
| **Style** | `solid thin`, `solid medium`, `solid thick`, `dashed medium` |
| **Fill** | `none`, `solid-black`, `color-fill(#3498DB)` |
| **Position** | Any zone from positioning system |

---

## Flat Design Aesthetic Guidelines

### DO ✓

```
✓ Use solid, flat colors from the standard palette
✓ Keep lines clean and uniform weight within element type
✓ Use simple geometric shapes with clear edges
✓ Maintain generous whitespace (minimum 10% margins)
✓ Include only elements that serve the learning purpose
✓ Use consistent styling across all elements
✓ Make the main subject fill 50-80% of the canvas
```

### DON'T ✗

```
✗ Add gradients, shadows, or 3D effects
✗ Use photorealistic textures or images
✗ Include decorative elements that don't support learning
✗ Make lines too thin (<1px) or too thick (>4px)
✗ Crowd elements together (maintain spacing)
✗ Use colors outside the standard palette
✗ Add extra boxes, circles, or shapes not specified
✗ Include embedded text (AI-generated text is unreliable)
```

### Visual Comparison

| Feature | ✓ Correct | ✗ Incorrect |
|---------|-----------|-------------|
| Background | Pure white (#FFFFFF) | Gray, textured, gradient |
| Lines | Solid, uniform weight | Varying thickness, sketchy |
| Shapes | Clean geometric edges | Rounded, beveled, 3D |
| Colors | Flat palette colors | Gradients, shadows |
| Text | None (add in post-processing) | AI-generated labels |

---

## Layout and Composition

### Spatial Guidelines

| Principle | Guideline |
|-----------|-----------|
| **Balance** | Visually balanced composition |
| **Whitespace** | Minimum 10% margin on all sides |
| **Hierarchy** | Most important elements largest and centered |
| **Alignment** | All elements aligned to invisible grid |
| **Proximity** | Related elements grouped together |

### Size Recommendations

| Context | Recommended Size |
|---------|------------------|
| Inline illustration | 300-400px width |
| Full-width diagram | 600-800px width |
| Hero graphic | 800-1000px width |
| Icon/symbol | 50-100px |
| Infographic | 600px × 800px (portrait) |

### Aspect Ratios

| Graphic Type | Aspect Ratio |
|--------------|--------------|
| Scientific diagram | 4:3 (landscape) |
| Process diagram | 16:9 (wide) |
| Comparison | 1:1 (square) or 2:1 |
| Infographic | 3:4 (portrait) |
| Graph | 4:3 or 1:1 (square) |

---

## Accessibility Requirements

### Visual Accessibility

| Requirement | Implementation |
|-------------|----------------|
| **Color independence** | Never use color as sole indicator |
| **Contrast** | Minimum 4.5:1 for text |
| **Pattern differentiation** | Use patterns + colors for categories |
| **Text alternatives** | Provide alt-text descriptions |

### Alt-Text Guidelines

Write alt-text that:
- Describes the essential information conveyed by the graphic
- Starts with the type of graphic ("Diagram showing...", "Graph of...")
- Includes key data points for graphs
- Mentions relationships or patterns illustrated
- Is concise (under 150 characters ideal; under 250 max)

```
---ALT-TEXT EXAMPLE---
Graphic Type: Line graph
Alt-Text: "Line graph showing speed (y-axis, 0-20 m/s) versus time (x-axis, 0-10 seconds). 
Line starts at origin, rises steadily to 15 m/s at 6 seconds, then remains constant until 10 seconds."
---END ALT-TEXT---
```

---

## Topic-Specific Visual Patterns

### Motion and Forces

| Concept | Standard Visual |
|---------|----------------|
| Velocity | Horizontal arrow, length proportional to speed |
| Acceleration | Series of arrows increasing/decreasing in length |
| Forces | Arrows from point of application |
| Free body | Object with multiple force arrows from center |
| Projectile motion | Parabolic path with velocity vectors |

### Waves and Optics

| Concept | Standard Visual |
|---------|----------------|
| Transverse wave | Sinusoidal curve on equilibrium line |
| Longitudinal wave | Compression/rarefaction pattern |
| Ray diagrams | Solid lines for real rays, dashed for virtual |
| Wave properties | Labeled wavelength (λ), amplitude (A) |
| Interference | Overlapping waves showing constructive/destructive |

### Electricity and Magnetism

| Concept | Standard Visual |
|---------|----------------|
| Circuits | IEC symbols, rectangular layout |
| Current flow | Arrow showing conventional current direction |
| Magnetic field | Lines from N to S with arrows |
| Electric field | Lines from + to − with arrows |
| Electromagnetic induction | Coil with field lines and motion indicators |

### Thermal Physics

| Concept | Standard Visual |
|---------|----------------|
| Particle motion | Dots with motion lines, spacing shows state |
| Heat transfer | Wavy arrows for radiation, straight for conduction |
| State changes | Particle arrangement in solid/liquid/gas |
| Energy diagrams | Bar charts or Sankey diagrams |

### Nuclear Physics

| Concept | Standard Visual |
|---------|----------------|
| Atomic structure | Nucleus (circle) with electron shells (rings) |
| Radioactive decay | Parent → products with decay arrow |
| Nuclear equations | Before/after with conservation shown |
| Half-life | Exponential decay curve |

---

## Integration with Module Creation

### Visual Requirements by Section

| Module Section | Visual Content |
|----------------|----------------|
| **Hook/Introduction** | Engaging real-world image or photo |
| **Core Content** | Conceptual diagrams, annotated equations |
| **Worked Examples** | Step diagrams, equation graphics |
| **Check Understanding** | Interactive graphics |
| **Summary** | Infographic, concept map |
| **Practice Exercises** | Exam-style diagrams (see Diagram Generation Spec) |

### Graphic Frequency Guidelines

| Content Length | Recommended Visuals |
|----------------|---------------------|
| Per major concept | 1-2 graphics |
| Per worked example | 1 diagram (if relevant) |
| Per formative quiz | 1-2 graphics |
| Per module summary | 1 overview visual (concept map or infographic) |

### Linking Graphics to Text

```
**Correct Pattern:**
[Text explains concept] → [Graphic illustrates concept] → [Text references graphic]

"As shown in Fig. 2.3, the current flows from..."
"See Fig. 2.3 for a visual representation."
"Compare your answer with the diagram in Fig. 2.3."
```

### Figure Numbering

Format: `Fig. [Module].[Sequential Number]`

Examples:
- Fig. 2.1, Fig. 2.2, Fig. 2.3... (Module 2, first section)
- Fig. 2.4, Fig. 2.5... (Module 2, second section)

---

## Quality Validation Checklist

### Pedagogical Effectiveness

- [ ] Graphic directly supports the learning objective
- [ ] Visual adds information not easily conveyed by text
- [ ] Complexity is appropriate for target audience
- [ ] Key elements are emphasized through visual hierarchy
- [ ] No decorative elements that don't support learning

### Technical Accuracy

- [ ] Scientific content is correct
- [ ] Symbols and conventions follow standards
- [ ] Units are displayed correctly
- [ ] Proportions are reasonable (if applicable)
- [ ] Labels are accurate and complete

### Visual Quality

- [ ] Clean lines, no pixelation
- [ ] Consistent style throughout module
- [ ] Colors used purposefully
- [ ] Sufficient contrast for readability
- [ ] Professional appearance

### Accessibility

- [ ] Color is not sole indicator of information
- [ ] Text meets contrast requirements
- [ ] Alt-text provided
- [ ] Adequately sized for viewing

### Integration

- [ ] Figure number assigned
- [ ] Caption is clear and educational
- [ ] Placed near relevant text
- [ ] Referenced in surrounding text

---

## Common Errors to Avoid

### Content Errors
❌ Decorative graphics that don't support learning  
❌ Overly complex visuals that increase cognitive load  
❌ Visual style inconsistent with rest of module  
❌ Graphics placed far from related text  
❌ Missing or inadequate figure captions  

### Technical Errors
❌ Incorrect physics representations  
❌ Non-standard symbols or conventions  
❌ Missing labels or units  
❌ Pixelated or low-resolution images  
❌ Unreadable text size  

### Accessibility Errors
❌ Color as only means of conveying information  
❌ Poor color contrast  
❌ Missing alt-text  
❌ Graphics too small to read details  

---

## Related Specifications

| Document | Relationship |
|----------|--------------|
| `IGCSE_Physics_Diagram_Generation_Spec.md` | Exam-style diagrams (circuits, rays, graphs, forces, fields, apparatus) |
| `IGCSE_Physics_Module_Creation_Spec.md` | Parent document defining module structure; inline diagram description template |
| `IGCSE_Physics_Exercise_Generation_Spec.md` | Questions that may reference graphics |

---

## Summary

This specification provides comprehensive guidelines for creating educational graphics in IGCSE Physics modules. Key principles:

1. **Purposeful** — Every graphic must support learning, not decorate
2. **Consistent** — Use standardized visual patterns across all modules
3. **Clear** — Prioritize clarity and simplicity over visual complexity
4. **Accessible** — Ensure all learners can access the information
5. **Integrated** — Graphics work seamlessly with surrounding text and activities

For exam-style technical diagrams (circuits, ray diagrams, graphs), refer to the companion `IGCSE_Physics_Diagram_Generation_Spec.md` for detailed conventions and templates.
