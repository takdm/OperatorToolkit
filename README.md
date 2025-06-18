# OperatorToolkit

A simple toolkit with calculation utilities for operators.

## Features

- **Trimcalc:**  
  Calculates trim size and trim weight based on user input for MR size, slit roll size (in mm), number of slits, and label roll weight.

- **PartCalc:**  
  Calculates partial roll weight and total partials based on user input for full roll footage, full roll weight, partial footage, and number of lanes.

## Usage

1. Run the program:
   ```
   python OpToolKit.py
   ```
2. The main menu will appear with the following options:
   - Select `1` to run Trimcalc. (useful at the beginning of a setup for paperwork)
   - Select `2` to run PartCalc. (useful during master roll changes)
   - Select `3` to exit the program.

3. Follow the prompts for each calculation.

## Structure

- `OpToolKit.py`: Main script containing all functions and the interactive menu.
- `README.md`: Project documentation.
