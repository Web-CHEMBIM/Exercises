# IGCSE Physics Diagram Generation Specification

## Overview

**Purpose:** AI Agent specifications for generating CAIE IGCSE Physics exam-style diagrams  
**Syllabus:** Cambridge IGCSE Physics (0625/0972)  
**Standard:** IEC 60617 and CAIE examination conventions  

This specification provides detailed guidelines for generating accurate, consistent, and professionally formatted physics diagrams that align with Cambridge Assessment International Education (CAIE) examination standards.

---

## Core Design Principles

### Visual Style Requirements

> **STYLE: Hand-Drawn with Clean White Background**
> 
> All diagrams should emulate the authentic hand-drawn aesthetic found in CAIE past papers while maintaining clarity and precision. The background MUST be pure white (#FFFFFF) with no textures, gradients, or noise.

| Aspect | Specification |
|--------|--------------|
| **Background** | **Pure white (#FFFFFF)** — no textures, no gray tones, no paper effects |
| **Line Style** | **Hand-drawn appearance** — slight natural variation in strokes, not perfectly computer-straight |
| **Line Weight** | Thin to medium; consistent within each diagram type |
| **Line Quality** | Solid black (#000000) for real elements; dashed for virtual/construction |
| **Precision** | Rays within 1mm of relevant points; angles accurate to ±2° |
| **Whitespace** | Generous margins; uncluttered layout |
| **Scale** | Fill at least 50% of allocated space |
| **Anti-aliasing** | Smooth edges but maintain hand-drawn character |

### Hand-Drawn Style Guidelines

```
DO:
✓ Use slightly imperfect lines (natural hand variation)
✓ Allow minor wobble in long straight lines
✓ Make arrowheads look hand-sketched
✓ Keep curves smooth but organic
✓ Use consistent stroke weight within a diagram

DON'T:
✗ Use perfectly computer-generated straight lines
✗ Add paper texture or background noise
✗ Include drop shadows or 3D effects
✗ Use gradient fills
✗ Add any color (black/white only)
✗ Make lines look like vector graphics
✗ Render grid lines, coordinates, or axis markers from GRID references
```

### Reference Aesthetic

The target look matches hand-drawn diagrams in:
- CAIE IGCSE Physics past papers (Papers 2, 4, 6)
- Clean whiteboard/blackboard teaching diagrams
- Technical sketches made with pencil and ruler on white paper

### Drawing Tool Simulation

When generating diagrams, simulate the use of proper drawing instruments:

| Tool | Application |
|------|-------------|
| **Sharp HB Pencil** | All lines and labels |
| **Ruler** | Straight lines, rays, axes, label lines |
| **Protractor** | Angle measurements and constructions |
| **Compasses** | Circles, arcs, curved mirrors |

---

## Structured Prompt Template System

> **CRITICAL: Use this structured format for ALL diagram descriptions to ensure AI generates accurate, consistent diagrams.**

### Universal Header (Required for ALL Diagrams)

Every diagram description MUST begin with this header:

```
---DIAGRAM: Fig. [N]---
TYPE: [Circuit | Ray | Graph | Force | Field | Apparatus | Wave | Particle]
PURPOSE: [One-line description of what diagram demonstrates]
STYLE: Hand-drawn aesthetic, solid black lines on pure white (#FFFFFF) background
ASPECT_RATIO: [4:3 landscape | 3:4 portrait | 16:9 wide | 1:1 square]
GRID: [columns] × [rows] (invisible reference grid for positioning)
```

> [!CAUTION]
> **GRID IS FOR INTERNAL POSITIONING REFERENCE ONLY.**  
> The final rendered image must **NOT** display grid lines, axis markers, coordinate numbers, or any visual representation of the grid system. The grid notation exists solely to help describe element positions in the prompt.

### Seven-Layer Description Structure

Describe diagrams in this EXACT order to ensure clarity:

| Layer | Purpose | Required? |
|-------|---------|-----------|
| 1. **HEADER** | Diagram type, purpose, style, dimensions | ✓ Always |
| 2. **CANVAS** | Background, aspect ratio, grid setup | ✓ Always |
| 3. **LAYOUT** | Overall arrangement pattern | ✓ Always |
| 4. **COMPONENTS** | Each element with full attributes | ✓ Always |
| 5. **CONNECTIONS** | Wires, rays, lines between elements | If applicable |
| 6. **LABELS** | Text annotations and values | ✓ Always |
| 7. **ANNOTATIONS** | Additional markings, arrows, notes | If applicable |

### Grid-Based Positioning System

Use a coordinate grid to specify EXACT positions:

```
GRID COORDINATE SYSTEM:
• Grid origin (1,1) is at TOP-LEFT corner
• X increases LEFT to RIGHT
• Y increases TOP to BOTTOM
• Format: grid(column, row) or grid(x, y)
• Ranges: grid(x1-x2, y1-y2) for spanning elements

Example 12×9 grid layout:
    1   2   3   4   5   6   7   8   9  10  11  12
  +---+---+---+---+---+---+---+---+---+---+---+---+
1 |   |   |   |   |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+---+---+---+---+
2 |   |   |   |   |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |   |   |   |   |
  ... (continues to row 9)
```

### Zone-Based Alternative

For simpler diagrams, use zone descriptions:

```
ZONES:
┌─────────────┬─────────────┬─────────────┐
│  top-left   │  top-center │  top-right  │
├─────────────┼─────────────┼─────────────┤
│ center-left │   center    │center-right │
├─────────────┼─────────────┼─────────────┤
│ bottom-left │bottom-center│bottom-right │
└─────────────┴─────────────┴─────────────┘
```

### Component Attribute Format

For EACH component, specify ALL attributes:

```
[Component Name]
  Symbol: [exact symbol description]
  Position: grid(x, y) or zone description
  Size: [dimensions in grid units or relative size]
  Orientation: [horizontal | vertical | angle in degrees]
  Style: [solid | dashed | dotted] [line weight: thin | medium | thick]
  Fill: [hollow | solid black | hatched | none]
  Label: "[text]" positioned [above | below | left | right | inside]
```

### Connection/Wire Format

For connections between elements:

```
[Wire/Ray/Line ID]
  Start: [element name or grid position]
  End: [element name or grid position]
  Path: [straight | right-angle | curved]
  Waypoints: [list of grid positions if path is complex]
  Style: [solid | dashed] [thin | medium | thick]
  Arrow: [none | single at end | single at start | double]
  Label: "[text]" at [start | middle | end]
```

### Label Format

For text annotations:

```
[Label ID]
  Text: "[exact text to display]"
  Target: [what this labels]
  Position: [above | below | left | right | at] [target or grid position]
  Leader: [yes | no] (connecting line to target)
  Style: [normal | italic | bold]
```

---

## Complete Structured Templates by Diagram Type

### Circuit Diagram Template

```
---DIAGRAM: Fig. [N]---
TYPE: Circuit
PURPOSE: [e.g., "Resistance measurement with ammeter and voltmeter"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: 4:3 landscape
GRID: 12 × 9

CANVAS:
  Background: pure white, no texture
  Border: none

LAYOUT:
  Shape: [rectangular loop | complex network]
  Current Flow: [clockwise | counterclockwise] conventional current

COMPONENTS:
  [Battery]
    Symbol: Two parallel lines (long thin = +, short thick = −)
    Position: grid(1, 4-6)
    Orientation: vertical, + terminal at top
    Label: "[voltage]V" left of symbol

  [Ammeter]
    Symbol: Circle containing capital "A"
    Position: grid(x, y)
    Size: 1.5 grid units diameter
    Connection: in series with [component]
    Reading: "[value]" displayed inside

  [Voltmeter]
    Symbol: Circle containing capital "V"
    Position: grid(x, y)
    Size: 1.5 grid units diameter
    Connection: in parallel across [component]
    Reading: "[value]" displayed inside

  [Resistor R]
    Symbol: Rectangle (IEC standard)
    Position: grid(x, y1-y2)
    Orientation: [horizontal | vertical]
    Style: hollow rectangle, black outline
    Label: "R" [position relative to symbol]

  [Switch S]
    Symbol: [Open: gap with raised lever | Closed: lever touching contact]
    Position: grid(x, y)
    State: [open | closed]
    Label: "S" above symbol

CONNECTIONS:
  [W1] Battery(+) → grid(x1,y1) → [direction] → grid(x2,y2) → Component(terminal)
  [W2] Component → grid(x,y) → [next component]
  
  Junction Style: solid black dot where 3+ wires meet
  Wire Style: solid black, consistent weight, 90° angles only
  Crossing Style: small arc where wires cross without connecting

CURRENT_ARROW:
  Position: on wire [W1] at grid(x, y)
  Direction: [compass direction or clockwise/counterclockwise indicator]
---END DIAGRAM---
```

### Ray Diagram Template

```
---DIAGRAM: Fig. [N]---
TYPE: Ray Diagram
PURPOSE: [e.g., "Image formation by converging lens, object beyond 2F"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: 16:9 wide
GRID: 20 × 9

CANVAS:
  Background: pure white
  Center Line: row [y] is the principal axis

LAYOUT:
  Optical Element: [lens | mirror] at grid column [x]
  Object Side: left of optical element
  Image Side: right of optical element

OPTICAL AXIS:
  Type: solid horizontal line
  Position: grid(1, 5) to grid(20, 5)
  Extends: full width of diagram

OPTICAL ELEMENT:
  [Converging Lens]
    Symbol: vertical line with outward arrows at top and bottom
    Position: grid(10, 3-7) centered on axis
    Label: none

REFERENCE POINTS:
  [F left]
    Position: grid(7, 5)
    Symbol: small dot on axis
    Label: "F" below axis
  
  [F right]
    Position: grid(13, 5)
    Symbol: small dot on axis
    Label: "F" below axis
  
  [2F left]
    Position: grid(4, 5)
    Symbol: small dot on axis
    Label: "2F" below axis
  
  [2F right]
    Position: grid(16, 5)
    Symbol: small dot on axis
    Label: "2F" below axis

OBJECT:
  Symbol: upright arrow pointing up
  Position: base at grid(3, 5), tip at grid(3, 3)
  Style: solid line with arrowhead at top
  Label: "O" at arrow tip

RAYS:
  [Ray 1 - Parallel Ray]
    Start: object tip grid(3, 3)
    Segment 1: grid(3, 3) → grid(10, 3), horizontal, solid
    Segment 2: grid(10, 3) → through F right → continues to grid(18, y)
    Arrow: on each segment, pointing left-to-right
    Style: solid line

  [Ray 2 - Central Ray]
    Start: object tip grid(3, 3)
    Path: straight line through lens center grid(10, 5)
    End: continues to grid(x, y)
    Arrow: pointing left-to-right
    Style: solid line

IMAGE:
  Position: where Ray 1 and Ray 2 intersect
  Symbol: [solid arrow if real | dashed arrow if virtual]
  Direction: [pointing down if inverted | pointing up if upright]
  Label: "I" at arrow tip
  Properties: [real/virtual], [inverted/upright], [magnified/diminished/same size]
---END DIAGRAM---
```

### Graph Template

> [!IMPORTANT]
> **SQUARE GRID CELLS ARE MANDATORY**
> Every graph MUST have visually square grid cells. This means:
> - The number of major divisions on the X-axis MUST equal the number on the Y-axis
> - Each grid cell must appear as a perfect square in the rendered image
> - This ensures accurate gradient perception and easier value interpolation

#### Grid Cell Proportions Rule

To achieve square grid cells, follow this calculation:
1. Determine the data range for each axis
2. Choose the **same number of major divisions** for both axes
3. Adjust axis range endpoints if necessary to create clean intervals

**Example:**
- If X-range needs 0 to 6 (6 divisions), and Y-data goes from 0 to 0.5
- Use Y-range 0 to 0.6 with 6 divisions (intervals of 0.1)
- This creates a 6×6 grid with square cells

```
---DIAGRAM: Fig. [N]---
TYPE: Graph
PURPOSE: [e.g., "I-V characteristics comparison of resistor, lamp, and diode"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)

CANVAS:
  Background: pure white
  Plot Area: SQUARE proportions (physical width = physical height)

GRID_CELLS:
  Shape: SQUARE (MANDATORY - each cell must be visually square)
  Major Divisions: [N] × [N] (SAME count on both axes, e.g., 6 × 6)
  Minor Subdivisions: [optional, e.g., 2 per major cell]
  Line Style: thin light gray (#CCCCCC)

AXES:
  [X-Axis]
    Label: "[Quantity] / [unit]" centered below axis
    Range: [min] to [max]
    Major Divisions: [N] divisions (MUST MATCH Y-axis count)
    Interval: [value per division]
    Ticks: labeled at each major division
    Arrow: small arrowhead at right end

  [Y-Axis]
    Label: "[Quantity] / [unit]" rotated 90°, left of axis
    Range: [min] to [max]
    Major Divisions: [N] divisions (MUST MATCH X-axis count)
    Interval: [value per division]
    Ticks: labeled at each major division
    Arrow: small arrowhead at top end

  [Origin]
    Position: bottom-left corner of plot area
    Label: "0" at origin (if axes start at 0)

DATA_POINTS:
  Symbol: small crosses (×) or circled dots (⊙)
  Coordinates: list as (x, y) values
  Accuracy: plotted within ½ small square of true position

CURVES/LINES:
  [Line 1]
    Name: "[component/scenario name]"
    Type: [best-fit line | smooth curve | line segments]
    Shape: [straight through origin | curved | exponential decay | etc.]
    Style: solid line, medium thickness
    
  [Line 2] (if applicable)
    Name: "[component/scenario name]"
    Type: [description]
    Style: dashed line, medium thickness

LEGEND (if multiple curves):
  Position: top-right area, inside plot
  Border: simple rectangle
  Contents:
    - solid line sample: "[Line 1 name]"
    - dashed line sample: "[Line 2 name]"

ANNOTATIONS (if applicable):
  [Point Labels]
    - Point "A" at (x, y): "[description]"
    - Point "B" at (x, y): "[description]"
  
  [Special Markings]
    - Gradient triangle showing Δy/Δx calculation
    - Half-life marker with horizontal dashed line
    - Intercept labels
---END DIAGRAM---
```

#### Common Graph Configurations (Square Grid Examples)

| Data Type | X-Range | Y-Range | Divisions | Cell Content |
|-----------|---------|---------|-----------|--------------|
| I-V Characteristic | 0 to 6 V | 0 to 0.6 A | 6 × 6 | 1 V and 0.1 A per cell |
| Distance-Time | 0 to 10 s | 0 to 50 m | 5 × 5 | 2 s and 10 m per cell |
| Decay Curve | 0 to 4 half-lives | 0 to 100% | 4 × 4 | 1 half-life and 25% per cell |
| Speed-Time | 0 to 8 s | 0 to 40 m/s | 4 × 4 | 2 s and 10 m/s per cell |

### Force Diagram Template

```
---DIAGRAM: Fig. [N]---
TYPE: Force Diagram
PURPOSE: [e.g., "Forces on block on inclined plane"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: 4:3 landscape
GRID: 12 × 9

CANVAS:
  Background: pure white

LAYOUT:
  Object: centered in diagram
  Force arrows: extending from object

OBJECT:
  Shape: [rectangle | circle | irregular shape description]
  Position: grid(5-8, 4-6)
  Style: solid outline, hollow interior
  Center of Mass: marked with small × at grid(6.5, 5)

SURFACE (if applicable):
  Type: [horizontal | inclined at angle θ]
  Position: grid(1, 7) to grid(12, 7) OR angled
  Style: solid line with hatching below

FORCES:
  [Weight W]
    Type: force arrow
    Start: center of mass grid(6.5, 5)
    Direction: vertically downward
    Length: [proportional to magnitude, e.g., 3 grid units]
    Arrow: solid arrowhead at end
    Label: "W = [value] N" right of arrow

  [Normal R]
    Type: force arrow
    Start: contact point grid(6.5, 6)
    Direction: perpendicular to surface
    Length: [proportional to magnitude]
    Arrow: solid arrowhead at end
    Label: "R" at arrow tip

  [Friction f]
    Type: force arrow
    Start: contact point grid(6.5, 6)
    Direction: along surface, opposing motion
    Length: [proportional to magnitude]
    Arrow: solid arrowhead at end
    Label: "f" at arrow tip

SCALE (if to scale):
  Notation: "1 cm represents [value] N"
  Position: bottom-right corner
---END DIAGRAM---
```

### Field Diagram Template

```
---DIAGRAM: Fig. [N]---
TYPE: Field Diagram
PURPOSE: [e.g., "Magnetic field pattern around bar magnet"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: 4:3 landscape
GRID: 12 × 9

CANVAS:
  Background: pure white

SOURCE:
  [Bar Magnet]
    Shape: rectangle
    Position: grid(4-9, 4-6)
    Style: solid outline
    Poles:
      - Left end: label "N" (north)
      - Right end: label "S" (south)

FIELD LINES:
  Pattern: curved lines from N to S externally
  Quantity: [6-8 lines showing pattern]
  
  [Line 1]
    Start: N pole, top edge
    Path: curves outward and around to S pole, top edge
    Arrow: pointing from N toward S (at midpoint)
  
  [Line 2]
    Start: N pole, middle
    Path: curves outward wide arc to S pole, middle
    Arrow: pointing from N toward S
  
  [Continue pattern for remaining lines...]

  Line Style: solid, thin
  Line Spacing: closer near poles, wider far from magnet

SPECIAL FEATURES:
  [Neutral Point] (if applicable)
    Position: grid(x, y)
    Marking: small × or labeled point
---END DIAGRAM---
```

### Apparatus Diagram Template

```
---DIAGRAM: Fig. [N]---
TYPE: Apparatus
PURPOSE: [e.g., "Setup to measure specific heat capacity of water"]
STYLE: Hand-drawn, solid black lines on pure white (#FFFFFF)
ASPECT_RATIO: 3:4 portrait
GRID: 9 × 12

CANVAS:
  Background: pure white

LAYOUT:
  Arrangement: [vertical stack | horizontal layout | custom]
  Main apparatus: centered

COMPONENTS:
  [Clamp Stand]
    Position: grid(2, 1-12)
    Elements:
      - Vertical rod: grid(2, 1-12)
      - Horizontal arm: grid(2-5, 3)
      - Clamp: at grid(5, 3)

  [Beaker]
    Shape: trapezoid (wider at top)
    Position: grid(4-8, 6-10)
    Contents: cross-hatched pattern for liquid
    Label: "water" inside or with leader

  [Thermometer]
    Shape: narrow rectangle with bulb at bottom
    Position: grid(6, 3-8), bulb submerged in liquid
    Scale: markings shown on shaft
    Reading: "[temperature]°C" shown

  [Heat Source]
    Type: [Bunsen burner | electric heater]
    Position: grid(5-7, 11)
    Symbol: [flame symbol | rectangular heater]
    Label: "heat" or "Bunsen burner"

  [Stirrer]
    Shape: thin rod
    Position: grid(7, 4-8)
    Label: "stirrer" if needed

MEASUREMENTS:
  [Thermometer Reading]
    Display: "[value]°C" visible on scale
  
  [Stopwatch] (if shown)
    Position: grid(8-9, 2)
    Display: "[time]" shown

ANNOTATIONS:
  [Heat Flow Arrow]
    From: heat source
    To: beaker bottom
    Style: wavy arrow
    Label: "heat" or "Q"

LABELS:
  - "water" → beaker contents
  - "thermometer" → thermometer
  - "Bunsen burner" → heat source
---END DIAGRAM---
```

---

## Diagram Type Catalog

### 1. Circuit Diagrams

#### Standard Component Symbols (IEC 60617)

| Component | Symbol Description | Key Features |
|-----------|-------------------|--------------|
| **Cell** | Two parallel lines (long thin = +, short thick = −) | Gap between lines |
| **Battery** | Multiple cells in series | Label voltage (e.g., 6V) |
| **Switch (Open)** | Gap in wire with lever raised | Clear gap visible |
| **Switch (Closed)** | Connected lever touching terminal | No gap |
| **Resistor** | Rectangle (IEC) or zigzag (US) | Use IEC rectangle for IGCSE |
| **Variable Resistor** | Resistor with diagonal arrow | Arrow through symbol |
| **Thermistor** | Resistor with small θ or T | Temperature indicator |
| **LDR** | Resistor in circle with arrows pointing in | Light arrows |
| **Lamp/Bulb** | Circle with cross inside | × inside ○ |
| **Ammeter** | Circle with letter A | Capital A centered |
| **Voltmeter** | Circle with letter V | Capital V centered |
| **Galvanometer** | Circle with letter G | Capital G centered |
| **Fuse** | Rectangle with thin line through center | OR thin wire symbol |
| **Diode** | Triangle with bar | Arrow shows current direction |
| **LED** | Diode with two arrows pointing outward | Light emission arrows |
| **Capacitor** | Two parallel lines (both same length) | Gap between |
| **Transformer** | Two coils with parallel lines between | Show primary/secondary |
| **Motor** | Circle with letter M | Capital M centered |
| **Generator** | Circle with letter G | Capital G centered |
| **Earth/Ground** | Three horizontal lines decreasing in length | Pointing downward |
| **Junction** | Solid dot where wires meet | Clear intersection |
| **Crossing (No Connect)** | Small arc over crossing wire | No dot |

#### Circuit Layout Rules

```
LAYOUT PRIORITIES:
1. Rectangular/Grid alignment — components on horizontal/vertical lines
2. Current flow — conventional current from + to − (clockwise typical)
3. Meter placement:
   • Ammeter: ALWAYS in series with measured component
   • Voltmeter: ALWAYS in parallel across measured component
4. Wire connections — clear 90° corners; no diagonal shortcuts
5. Component spacing — even distribution; avoid crowding
6. Labels — components labeled (R, A, V, etc.); values shown where relevant
```

#### Circuit Diagram Template

> **📌 Use the Structured Template:** For AI image generation, use the comprehensive **Circuit Diagram Template** in the "Complete Structured Templates by Diagram Type" section above. The format below is a legacy quick-reference.

```
---CIRCUIT DIAGRAM---
TITLE: [Name of circuit, e.g., "Series Circuit with Ammeter"]
COMPONENTS:
• [Component 1]: [Location description]
• [Component 2]: [Location description]
• [Ammeter A]: in series with [component]
• [Voltmeter V]: in parallel across [component]
CONNECTIONS:
• [Description of how components connect]
VALUES SHOWN:
• [Any readings, e.g., "Ammeter: 2.5 A", "Battery: 6V"]
CURRENT DIRECTION: [e.g., "clockwise from + terminal"]
LABELS: [A, V, R₁, R₂, etc.]
---END CIRCUIT---
```

#### Example: Simple Resistance Measurement Circuit

```
---CIRCUIT DIAGRAM---
TITLE: Resistance Measurement Circuit
COMPONENTS:
• Battery (6V): top left, + terminal facing right
• Switch S: top side, right of battery
• Variable resistor: right side, vertical
• Fixed resistor R: bottom side
• Ammeter A: bottom left, in series with R
• Voltmeter V: connected across R (parallel)
CONNECTIONS:
• Battery + → Switch → Variable resistor → bottom junction
• Bottom junction → Resistor R → Ammeter → Battery −
• Voltmeter connected from junction before R to junction after R
VALUES SHOWN:
• Battery labeled "6V"
• Ammeter shows "0.5 A"
• Voltmeter shows "3.0 V"
CURRENT DIRECTION: clockwise
LABELS: S, A, V, R, 6V
---END CIRCUIT---
```

---

### 2. Ray Diagrams (Optics)

#### General Optics Conventions

| Element | Style | Description |
|---------|-------|-------------|
| **Principal Axis** | Solid horizontal line | Extends beyond optical element |
| **Normal Line** | Dashed line | Perpendicular to surface at incidence point |
| **Real Rays** | Solid lines with arrows | Actual light path |
| **Virtual Rays** | Dashed lines | Extensions of real rays |
| **Object** | Upright arrow on axis | Arrow pointing upward |
| **Real Image** | Solid inverted/upright arrow | Where rays converge |
| **Virtual Image** | Dashed arrow | Where virtual rays appear to meet |
| **Focus (F)** | Point marked on axis | Label clearly |
| **Optical Center (C/O)** | Point at lens/mirror center | Label clearly |
| **2F Point** | Point at twice focal length | For image construction |

#### Lens Symbols

| Lens Type | Symbol | Key Feature |
|-----------|--------|-------------|
| **Converging (Convex)** | ◇ with arrows pointing OUT at ends | Thicker in middle |
| **Diverging (Concave)** | ◇ with arrows pointing IN at ends | Thinner in middle |

#### Key Ray Rules for Lenses

**Converging Lens (always draw at least 2 rays):**
1. **Parallel Ray:** Incident parallel to principal axis → refracts through F (far side)
2. **Central Ray:** Through optical center → passes straight (undeviated)
3. **Focal Ray:** Through F (near side) → emerges parallel to axis

**Diverging Lens:**
1. **Parallel Ray:** Incident parallel to axis → appears to diverge from F (near side)
2. **Central Ray:** Through center → undeviated
3. **Focal Ray:** Directed toward F (far side) → emerges parallel

#### Mirror Ray Rules

**Concave Mirror:**
1. Parallel to axis → reflects through F
2. Through F → reflects parallel to axis
3. Through C (center of curvature) → reflects back on itself

**Convex Mirror:**
1. Parallel to axis → reflects as if from F (behind mirror)
2. Toward F → reflects parallel to axis

#### Refraction Conventions

| Transition | Bending Direction | Angle Relationship |
|------------|-------------------|-------------------|
| Less dense → More dense | Toward normal | i > r |
| More dense → Less dense | Away from normal | r > i |
| Along normal | No bending | i = r = 0° |

#### Ray Diagram Template

```
---RAY DIAGRAM---
TYPE: [Converging Lens / Diverging Lens / Plane Mirror / Concave Mirror / Refraction]
SETUP:
• Principal axis: [horizontal line through center]
• Optical element: [position and type]
• Focal points: F marked at [distance] on [both sides / one side]
• Object O: [position relative to F and 2F], height [approximate]
RAYS DRAWN:
• Ray 1: [description, e.g., "parallel to axis, refracts through F"]
• Ray 2: [description, e.g., "through optical center, undeviated"]
• Ray 3 (optional): [description]
IMAGE:
• Position: [between F and 2F / beyond 2F / same side as object]
• Properties: [real/virtual], [upright/inverted], [magnified/diminished/same size]
• Representation: [solid arrow / dashed arrow]
LABELS: O, I, F, F', C, 2F, 2F'
ARROWS: [direction of light propagation on each ray]
---END RAY DIAGRAM---
```

#### Example: Converging Lens with Object Beyond 2F

```
---RAY DIAGRAM---
TYPE: Converging Lens
SETUP:
• Principal axis: horizontal line extending 15 cm either side
• Lens: vertical double-arrow symbol at center (0 cm)
• F marked at 4 cm left and 4 cm right of lens
• 2F marked at 8 cm left and 8 cm right
• Object O: upright arrow at 12 cm left of lens, height 2 cm
RAYS DRAWN:
• Ray 1: From top of O, parallel to axis → refracts through F on right
• Ray 2: From top of O, through center of lens → continues straight
• Rays intersect at position between F and 2F on right side
IMAGE:
• Position: approximately 6 cm right of lens
• Properties: real, inverted, diminished
• Representation: solid downward arrow where rays meet
LABELS: O, I, F, F, 2F, 2F, principal axis
ARROWS: All rays have arrows pointing left-to-right (light direction)
---END RAY DIAGRAM---
```

---

### 3. Graphs and Plots

#### Axis Conventions

| Axis | Content | Format |
|------|---------|--------|
| **X-axis (horizontal)** | Independent variable | "Quantity / unit" (e.g., "Time / s") |
| **Y-axis (vertical)** | Dependent variable | "Quantity / unit" (e.g., "Distance / m") |
| **Origin** | Start at (0,0) unless data requires offset | Clearly marked |
| **Scale** | Regular intervals (1, 2, 5, 10, 20, 50...) | Consistent throughout |
| **Grid** | Light gray lines if needed | Should not obscure data |

#### Plotting Standards

| Element | Standard |
|---------|----------|
| **Data Points** | Small, neat crosses (×) or circled dots (⊙) |
| **Point Accuracy** | Within ½ small square of true position |
| **Best-fit Line** | Smooth line (straight or curved) through trend |
| **Line Drawing** | Do NOT connect dot-to-dot; balance points above/below |
| **Outliers** | Circle and exclude from best-fit |
| **Line Extension** | Extrapolate only if question requires |

#### Physics Graph Types

##### Distance-Time Graph
```
• X-axis: "Time / s" (always)
• Y-axis: "Distance / m"
• Gradient = speed
• Horizontal line = stationary
• Straight sloped line = constant speed
• Curve = changing speed (acceleration/deceleration)
```

##### Speed-Time (Velocity-Time) Graph
```
• X-axis: "Time / s" (always)
• Y-axis: "Speed / m/s" or "Velocity / m/s"
• Gradient = acceleration
• Horizontal line = constant speed
• Area under line = distance traveled
• Below x-axis = motion in opposite direction (velocity only)
```

##### I-V Characteristics
```
• X-axis: "Potential difference / V" (typical) or Current
• Y-axis: "Current / A" (typical) or Voltage
• Gradient interpretation:
  - If I on y-axis: gradient = 1/R
  - If V on y-axis: gradient = R
```

| Component | I-V Graph Shape |
|-----------|----------------|
| **Ohmic Conductor (resistor)** | Straight line through origin |
| **Filament Lamp** | Curve that flattens at higher V (resistance increases with temp) |
| **Diode** | Almost flat at low V, sharp rise after threshold (~0.7V) |
| **Thermistor** | Depends on interpretation; typically non-linear |

##### Decay Curves (Radioactivity)
```
• X-axis: "Time / s" (or minutes, hours, days)
• Y-axis: "Activity / Bq" or "Count rate / counts per second" or "Number of nuclei"
• Shape: Exponential decay curve
• Half-life: Time for quantity to halve (mark on graph)
```

#### Graph Template

```
---GRAPH---
TYPE: [Distance-Time / Speed-Time / I-V Characteristic / Decay Curve / Custom]
AXES:
• X-axis: "[Quantity] / [unit]", range [min] to [max], scale [interval]
• Y-axis: "[Quantity] / [unit]", range [min] to [max], scale [interval]
• Origin: [at (0,0) / offset to (x, y)]
DATA POINTS (if applicable):
• Point 1: (x₁, y₁)
• Point 2: (x₂, y₂)
• [continue...]
CURVE/LINE:
• Shape: [straight line / smooth curve / stepwise]
• Key features: [gradient value, intercept, asymptote, half-life point]
ANNOTATIONS:
• [Label specific points, e.g., "A = start", "B = constant speed"]
• [Shaded areas if calculating distance/work]
SPECIAL MARKINGS:
• [Tangent lines, gradient triangles, half-life markers]
---END GRAPH---
```

---

### 4. Force and Field Diagrams

#### Force Diagram Conventions

| Element | Style |
|---------|-------|
| **Force Arrow** | Straight line with solid arrowhead |
| **Arrow Length** | Proportional to force magnitude |
| **Arrow Origin** | Point of application (usually center of mass for weight) |
| **Arrow Direction** | Direction force acts |
| **Labels** | Force name and value (e.g., "W = 50 N") |

#### Common Force Types

| Force | Symbol | Direction | Application Point |
|-------|--------|-----------|-------------------|
| **Weight** | W | Vertically downward | Center of mass |
| **Normal/Reaction** | R or N | Perpendicular to surface | Contact surface |
| **Friction** | F or f | Opposite to motion (along surface) | Contact surface |
| **Tension** | T | Along the string/rope | Point of attachment |
| **Air Resistance/Drag** | D | Opposite to motion | Center of mass |
| **Applied/Push/Pull** | F | Direction of push/pull | Point of application |
| **Upthrust** | U | Vertically upward | Center of submerged volume |

#### Force Diagram Template

```
---FORCE DIAGRAM---
OBJECT: [Description, e.g., "wooden block on inclined plane"]
FORCES:
• Weight W: downward from center of mass, magnitude [value] N
• Normal R: perpendicular to [surface], magnitude [value] N
• Friction F: along [surface] opposing motion, magnitude [value] N
• [Additional forces as needed]
RESULTANT (if required):
• Direction: [e.g., "down the slope"]
• Magnitude: [value] N
CENTER OF MASS: marked with [dot / cross / symbol]
SCALE: [e.g., "1 cm represents 10 N"] (if to scale)
---END FORCE DIAGRAM---
```

#### Magnetic Field Lines

| Source | Pattern Description |
|--------|---------------------|
| **Bar Magnet** | Curved lines from N pole to S pole externally; lines closest at poles |
| **Straight Wire (current)** | Concentric circles around wire; direction by right-hand grip rule |
| **Solenoid** | Bar magnet pattern; field lines inside are parallel and uniform |
| **Between Unlike Poles (N-S)** | Lines curve from N to S; attraction shown |
| **Between Like Poles (N-N or S-S)** | Lines repel; neutral point between poles |

#### Field Line Rules
```
1. Field lines NEVER cross
2. Lines go from N to S (magnetic) or + to − (electric)
3. Closer lines = stronger field
4. Arrows show field direction
5. Lines are continuous curves (closed loops for magnetic)
```

#### Field Diagram Template

```
---FIELD DIAGRAM---
TYPE: [Magnetic / Electric / Gravitational]
SOURCE: [e.g., "bar magnet", "parallel plates", "current-carrying wire"]
FIELD LINES:
• Pattern: [description of curve pattern]
• Direction: [arrows pointing N to S / + to −]
• Density: [closer near poles, uniform in center, etc.]
POLES/CHARGES: [labeled N, S, +, −]
SPECIAL FEATURES:
• [Neutral point location if applicable]
• [Uniform region indication]
---END FIELD DIAGRAM---
```

---

### 5. Apparatus Diagrams

#### General Apparatus Drawing Rules

```
1. Draw apparatus to fill available space (50-70%)
2. Use consistent line weights
3. Show 3D perspective where helpful (cross-sections)
4. Label all key components
5. Show measurement scales/readings where relevant
6. Include arrows for flows (heat, current, forces)
7. Use standard cross-hatching for solid sections
```

#### Standard Apparatus Elements

| Element | Representation |
|---------|---------------|
| **Beaker/Container** | U-shape or trapezoid outline |
| **Thermometer** | Narrow rectangle with bulb at bottom; scale markings |
| **Clamp Stand** | Vertical rod with horizontal arm; clamp indicated |
| **Heat Source (Bunsen)** | Flame symbol or labeled rectangle |
| **Stopwatch** | Circle with display or labeled box |
| **Ruler/Meter Rule** | Rectangle with scale markings |
| **Spring** | Zigzag or coil pattern |
| **Pulley** | Circle with groove; axle shown |
| **Masses/Weights** | Rectangles labeled with mass (e.g., "100 g") |
| **Wire/String** | Thin line (solid for wire, may use different style for string) |

#### Apparatus Diagram Template

```
---APPARATUS DIAGRAM---
EXPERIMENT: [Name/purpose]
COMPONENTS:
• [Component 1]: [location and orientation]
• [Component 2]: [location and orientation]
• [Measuring device]: [what it measures, position]
SETUP DESCRIPTION:
• [How components are connected/arranged]
• [What is being measured and how]
LABELS: [List all labels to include]
MEASUREMENTS SHOWN:
• [Scale readings, dimensions, values]
ANNOTATIONS:
• [Arrows for heat flow, direction of motion, etc.]
---END APPARATUS---
```

---

### 6. Wave Diagrams

#### Transverse Wave Elements

| Element | Representation |
|---------|---------------|
| **Wave Shape** | Smooth sinusoidal curve |
| **Wavelength (λ)** | Horizontal arrow between two equivalent points (crest to crest) |
| **Amplitude (A)** | Vertical arrow from equilibrium to peak |
| **Equilibrium Line** | Horizontal dashed line through middle |
| **Direction of Propagation** | Horizontal arrow showing wave travel direction |
| **Particle Motion** | Vertical double-arrow showing oscillation |

#### Longitudinal Wave Elements

| Element | Representation |
|---------|---------------|
| **Compressions** | Closely spaced vertical lines |
| **Rarefactions** | Widely spaced vertical lines |
| **Wavelength (λ)** | Distance from compression to compression |
| **Direction of Propagation** | Horizontal arrow |
| **Particle Motion** | Horizontal double-arrow (parallel to propagation) |

---

### 7. Nuclear and Particle Diagrams

#### Atomic Model Representations

| Model | Elements |
|-------|----------|
| **Nuclear Model** | Central nucleus (small circle), electron orbits (dashed circles) |
| **Nucleus Detail** | Protons (labeled p or +), Neutrons (labeled n or 0) |
| **Electron Shells** | Concentric circles with electrons marked |

#### Decay Representations

| Decay Type | Symbol | Diagram Elements |
|------------|--------|-----------------|
| **Alpha (α)** | ⁴₂He or ⁴₂α | Two protons + two neutrons leaving nucleus |
| **Beta-minus (β⁻)** | ⁰₋₁e or ⁰₋₁β | Electron emitted, antineutrino (optional) |
| **Gamma (γ)** | ⁰₀γ | Wavy line from nucleus; no particle change |

---

## ASCII/Text Diagram Examples

When generating text-based worksheets, use these ASCII patterns:

### Simple Circuit (ASCII)

```
    +─────────[A]─────────+
    │                     │
   ═╪═                    ○
   ═╪═ 6V                |/
    │                    (R)
    │                     │
    +──────────●──────────+
               │
              [V]
               │
               ●──────────────
```

### Lens Ray Diagram (ASCII)

```
                    F'        F
         O          │         │
    ─────┼──────────┼────◇────┼──────────┼─────
         │          │    │    │          │
     object      2F │    │    │ 2F    image
                    │   lens  │
```

### Force Diagram (ASCII)

```
              ↑ R (Normal)
              │
         ┌────┴────┐
         │  block  │ ← F (friction)
         └────┬────┘
              │
              ↓ W (Weight)
```

---

## Quality Validation Checklist

### Pre-Generation Checks

- [ ] Diagram type appropriate for question/topic?
- [ ] Required elements identified from learning objective?
- [ ] Correct conventions selected for diagram type?

### Structural Checks

- [ ] All standard symbols used correctly?
- [ ] Labels clear and positioned with straight label lines?
- [ ] Arrows show correct directions?
- [ ] Scale appropriate (fills 50%+ of space)?
- [ ] Lines clean and consistent weight?

### Physics Accuracy Checks

- [ ] Physical principles correctly represented?
- [ ] Measurements/values physically plausible?
- [ ] Directions correct (current flow, field lines, forces)?
- [ ] Conservation laws respected (if applicable)?

### Exam Style Checks

- [ ] Figure number assigned (e.g., "Fig. 1")?
- [ ] Brief caption included?
- [ ] Black and white only?
- [ ] Student task clear (complete/label/draw)?
- [ ] Mark allocation appropriate for diagram complexity?

---

## Integration with Exercise Generation

### When to Include Diagrams

Reference the main `IGCSE_Physics_Exercise_Generation_Spec.md` for:
- Diagram trigger detection (keywords)
- Diagram percentage requirements by question type
- Topic-specific diagram patterns

### Diagram Description Block Format

All diagrams should be described using this structured format:

```
---DIAGRAM: Fig. [X]---
DIAGRAM_TYPE: [Circuit / Ray / Graph / Force / Field / Apparatus / Wave / Particle]
[Type-specific template content from above]
---END DIAGRAM---
```

### Linking to Questions

```
Fig. X shows [brief description].

---DIAGRAM: Fig. X---
[Full diagram specification]
---END DIAGRAM---

(a) Using Fig. X, [question referencing diagram] [marks]
(b) On Fig. X, [completion/labeling task] [marks]
```

---

## Common Errors to Avoid

### Circuit Diagrams
❌ Ammeter in parallel (must be series)  
❌ Voltmeter in series (must be parallel)  
❌ Missing component labels  
❌ Diagonal wires (use 90° corners)  
❌ Wrong battery polarity notation  

### Ray Diagrams
❌ Rays not passing through required points (F, C)  
❌ Missing arrows on ray lines  
❌ Virtual rays drawn as solid lines  
❌ Forgetting to mark F and 2F points  
❌ Rays not meeting at image point  

### Graphs
❌ Axes not labeled with "Quantity / unit"  
❌ Dot-to-dot instead of best-fit line  
❌ Scale not starting at sensible value  
❌ Graph too small (less than half space)  
❌ Wrong variable on wrong axis  

### Force Diagrams
❌ Force arrows not from correct point  
❌ Arrows not proportional to magnitude  
❌ Missing force labels  
❌ Wrong direction for reaction forces  

---

## Summary

This specification provides comprehensive guidelines for generating IGCSE Physics exam-style diagrams. Key principles:

1. **Consistency** — Use standardized symbols and conventions throughout
2. **Precision** — Maintain accuracy requirements (1mm for rays, correct angles)
3. **Clarity** — Clean lines, clear labels, uncluttered layout
4. **Exam Alignment** — Follow CAIE marking scheme expectations
5. **Student Task** — Clearly indicate what students should do (interpret/complete/draw)

For integration with exercise generation, use the diagram description templates to create reproducible, accurate diagrams that match Cambridge examination standards.
