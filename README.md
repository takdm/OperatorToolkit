# OperatorToolkit

OperatorToolkit is a simple, interactive toolkit designed to help operators perform common calculations related to roll setup and partials in manufacturing or label production environments.

---

## Features

- **Trimcalc**  
  Calculate trim size and trim weight based on:
  - Master roll (MR) size (inches)
  - Slit roll size (mm)
  - Number of slits
  - Label roll weight

- **PartCalc**  
  Calculate partial roll weight and totals based on:
  - Full roll footage (feet)
  - Full roll weight
  - Partial footage (feet)
  - Number of lanes

---

## Getting Started

### Windows

1. Download and extract the release ZIP.
2. Run `OpToolKit.exe`.

### Linux / macOS / Other

1. Download and extract the source code.
2. Ensure you have Python 3 installed.
3. Run the toolkit from the terminal:
   ```
   python OpToolKit.py
   ```
4. Follow the on-screen menu:
   - `1` — Run Trimcalc (for setup calculations)
   - `2` — Run PartCalc (for partial roll calculations)
   - `3` — Exit

---

## Example Usage

**Trimcalc Example:**
```
Enter MR Size (inches): 40
Enter Slit Roll Size (mm): 100
Enter Number of Slits: 3
Enter Label Roll Weight: 50

Trim Size: 28.18 inches
Trim Weight: 35.23
```

**PartCalc Example:**
```
Enter full roll footage:
1000
Enter full roll weight:
200
Enter partial footage (rounded):
250
Enter amount of lanes:
2

Your per roll partial weight is 50.00
Your partials total at 100.00
...
```

---

## Project Structure

- `OpToolKit.py` — Main entry point and menu
- `Trimcalc.py` — Trim calculation logic
- `Partcalc.py` — Partial calculation logic
- `Menu.py` — Menu system (if used separately)
- `README.md` — Project documentation

---

## Requirements

- Python 3.x

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue to discuss changes or improvements.

---
