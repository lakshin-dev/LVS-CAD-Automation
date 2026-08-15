# Low Voltage Systems CAD Automation

> Python-based automation for generating CAD-compatible Single Line Diagram (SLD) layouts for CCTV and Fire Alarm systems.

## Overview

This project automates repetitive CAD layout operations involved in Low Voltage Systems (LVS) engineering documentation.

The core idea is simple:

**Engineering inputs → programmable layout rules → reusable CAD blocks → DXF output**

Instead of manually redrawing repeated symbols, floor sections, labels, spacing and equipment placement in AutoCAD, the generators accept structured floor-wise device counts and create parameter-driven DXF layouts.

The project was developed as an internship engineering-automation project.

---

## Projects

### 1. CCTV SLD Generator

Generates multi-floor CCTV Single Line Diagram layouts from floor-wise camera counts.

**Supported camera types**
- Dome Camera
- Bullet Camera

**Implemented features**
- Automatic Ground Floor generation
- Multi-floor layout generation
- Floor-wise Dome/Bullet camera input
- Camera-count validation
- Global camera scaling based on the most populated floor
- Full-size layout up to 16 cameras
- Progressive scaling between 17–23 cameras
- Two-box layout from 24 cameras onward
- Configurable maximum of 48 cameras per floor
- Dynamic camera-box width
- Right-side electrical-box placement
- Reusable camera blocks
- CAD-compatible DXF output

The implemented configuration uses:
- `DEFAULT_CAMERA_LIMIT = 16`
- `SHRINK_LIMIT = 24`
- `MAX_CAMERAS = 48`
- `MIN_CAMERA_SCALE = 0.65`

---

### 2. Fire Alarm SLD Generator

Generates multi-floor Fire Alarm Single Line Diagram layouts using floor-wise device counts.

**Supported devices**
- Smoke Detector
- Heat Detector
- Multi-Sensor Detector
- Manual Call Point (MCP)
- Hooter
- Monitor Module (MM)
- Control Module (CM)
- Relay Module (RM)

**Implemented features**
- Automatic Ground Floor generation
- Multi-floor generation
- Floor-wise device input
- Reusable CAD symbol blocks
- Separate hooter section
- Dynamic device-group width
- Centered device placement
- Global symbol scaling
- Parameterized floor dimensions and spacing
- CAD-compatible DXF output

The current configuration uses:
- Default scale: `1.0`
- Default device limit: `20`
- Shrink limit: `40`
- Minimum symbol scale: `0.65`

---

## System Architecture

The project uses a modular Python structure:

```text
                    Engineering Inputs
                           │
                           ▼
                      ┌─────────┐
                      │ main.py │
                      │ Input & │
                      │ Control │
                      └────┬────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ constants.py │
                    │ Configuration│
                    └──────┬───────┘
                           │
                           ▼
                      ┌─────────┐
                      │blocks.py│
                      │   CAD   │
                      │ Symbols │
                      └────┬────┘
                           │
                           ▼
                       ┌────────┐
                       │ draw.py │
                       │Geometry│
                       │ Layout │
                       └────┬───┘
                            │
                            ▼
                     ┌────────────┐
                     │ DXF Output │
                     └────────────┘
```

### Module responsibilities

| File | Responsibility |
|---|---|
| `constants.py` | Dimensions, limits, colors, spacing, block names and configuration |
| `blocks.py` | Reusable CAD symbol/block creation |
| `draw.py` | Geometry, scaling, positioning and layout generation |
| `main.py` | User input, validation, orchestration and DXF generation |

This separation makes layout parameters easier to modify without rewriting the complete drawing logic.

---

## How the Automation Works

### CCTV workflow

```text
Enter number of floors
        ↓
Collect Dome + Bullet counts
        ↓
Validate camera limit
        ↓
Collect all floor data
        ↓
Find maximum camera count
        ↓
Calculate global scale
        ↓
Determine single-row / two-box layout
        ↓
Generate floor boundaries and labels
        ↓
Insert camera blocks
        ↓
Place electrical box
        ↓
Save CCTV_LAYOUT.dxf
```

### Fire Alarm workflow

```text
Enter number of floors
        ↓
Collect eight device counts
        ↓
Store floor-wise data
        ↓
Find maximum device count
        ↓
Calculate global scale
        ↓
Build detector and hooter lists
        ↓
Calculate required box widths
        ↓
Generate floor boundaries and labels
        ↓
Place hooter row
        ↓
Place remaining device row
        ↓
Save FIRE_ALARM_LAYOUT.dxf
```

---

## Dynamic Layout Logic

A major part of the project is avoiding fixed screen positions.

### CCTV

The generator determines the global camera scale from the floor containing the highest number of cameras.

- `≤ 16` cameras → scale `1.0`
- `17–23` cameras → progressive scaling
- `≥ 24` cameras → two stacked camera boxes
- Minimum scale → `0.65`
- Maximum configured input → `48` cameras/floor

The camera area also reserves space for the right-side electrical box and the required gap.

### Fire Alarm

The Fire Alarm generator calculates a global symbol scale from the maximum device count across all floors.

The device-box width is calculated from:

```text
symbol width
+ inter-device spacing
+ horizontal padding
```

The wider requirement between the detector group and hooter group is used so that the two boxes align.

---

## Technologies Used

- **Python 3**
- **ezdxf**
- **AutoCAD / DXF workflow**
- **VS Code**

### Python concepts used

- Functions
- Lists and dictionaries
- Loops and conditional logic
- Input validation
- Coordinate geometry
- Mathematical scaling
- Modular program design
- File generation

### CAD concepts used

- DXF document creation
- Modelspace
- Reusable block definitions
- Block references
- Circles, arcs, lines and polylines
- Text placement
- Coordinates and geometric constraints
- Symbol scaling
- CAD layer/configuration concepts

---

## Project Structure

```text
LVS-CAD-Automation/
│
├── CCTV/
│   ├── constants.py
│   ├── blocks.py
│   ├── draw.py
│   ├── main.py
│   └── CCTV_LAYOUT.dxf
│
├── Fire-Alarm/
│   ├── constants.py
│   ├── blocks.py
│   ├── draw.py
│   ├── main.py
│   └── FIRE_ALARM_LAYOUT.dxf
│
├── outputs/
│   ├── CCTV_layout.pdf
│   └── Fire_Alarm_layout.pdf
│
└── README.md
```

> The exact folder structure can be adjusted depending on how the repository is organized.

---

## Installation

Install Python 3 and the required package:

```bash
pip install ezdxf
```

Clone the repository:

```bash
git clone <YOUR-REPOSITORY-URL>
cd LVS-CAD-Automation
```

---

## Running the Generators

### CCTV

Navigate to the CCTV project directory and run:

```bash
python main.py
```

The program asks for:

1. Number of floors excluding Ground
2. Dome camera count per floor
3. Bullet camera count per floor

The generated file is:

```text
CCTV_LAYOUT.dxf
```

### Fire Alarm

Navigate to the Fire Alarm project directory and run:

```bash
python main.py
```

The program asks for the number of each supported device on every floor.

The generated file is:

```text
FIRE_ALARM_LAYOUT.dxf
```

---

## Example Output

### CCTV

The generated layout contains:
- Floor boundaries
- Ground Floor and upper-floor labels
- Camera grouping boxes
- Dome and Bullet camera symbols
- Right-side electrical boxes
- Adaptive camera scaling

### Fire Alarm

The generated layout contains:
- Floor boundaries
- Floor labels
- Detector/device grouping
- Separate hooter row
- Reusable device symbols
- Dynamic group widths
- Adaptive global scaling

---

## Engineering Problem Solved

The project addresses a repetitive drafting problem:

> How can repeated CAD drawing operations be converted into a parameter-driven process so that changing floor counts or device counts does not require manually redrawing the entire SLD?

The solution represents drawing requirements as programmable rules for:

- Symbol generation
- Spacing
- Alignment
- Scaling
- Box dimensions
- Floor placement
- Label placement
- Device grouping

The result is a reusable CAD-generation workflow rather than a fixed drawing.

---

## Validation and Testing

Validation was performed through repeated execution and visual inspection of generated layouts.

The development process included checking:

- Camera/device count constraints
- Global scale calculation
- Floor alignment
- Label placement
- Device spacing
- Camera-box placement
- Electrical-box separation
- Hooter/device grouping
- Generated DXF output
- Overall drawing readability

A successful run produces the corresponding DXF file after the drawing-generation stage.

---

## Limitations

The current implementation is a functional automation prototype rather than a complete commercial CAD automation platform.

Current limitations include:

- Command-line input
- No Excel/CSV project-data import
- Limited automatic validation of engineering inputs
- No complete wire/riser routing engine
- No automatic title-block/legend generation
- Limited collision detection
- No automated regression comparison against reference drawings

---

## Future Scope

Possible extensions include:

- GUI-based input
- Excel/CSV integration
- Automated project-data validation
- Automatic legends and title blocks
- Expanded standardized symbol libraries
- Advanced wire/riser routing
- CAD layer management
- Collision detection and adaptive placement
- Automated regression testing
- Integration with larger LVS drawing workflows

---

## Key Learning

The main learning from this project was not simply using Python to draw CAD geometry.

It was the process of converting a visual engineering requirement into a set of **explicit, reusable computational rules**.

For example:

```text
"Keep the electrical box separated"
            ↓
Coordinate + gap constraint

"Fit more cameras"
            ↓
Scaling + row-layout logic

"Keep floor labels consistent"
            ↓
Parameterized label generation

"Use the same device symbol repeatedly"
            ↓
Reusable CAD block references
```

This approach turned repetitive drafting operations into a small rule-based layout engine.

---

## Project Status

**Status:** Functional prototype

**Output:** CAD-compatible DXF layouts

**Primary focus:** Engineering drawing automation

**Domains:** Low Voltage Systems, CAD Automation, Python Automation

---

## Author

**Lakshin Punilan**  
B.Tech Electronics and Computer Engineering  
VIT Chennai

---

## Note on Public Repository Content

This repository should contain only code, sample outputs and documentation that are permitted to be shared publicly.

Any company-specific drawings, client information, internal standards, proprietary data or confidential project files should be removed or anonymized before publishing.
