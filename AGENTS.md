# AGENTS.md - Operator Toolkit

This document provides guidelines for agentic coding agents working on the Operator Toolkit project.

## Project Overview

Operator Toolkit is a Python-based manufacturing calculator application with both GUI and console interfaces. It helps operators perform calculations related to roll setup, partials, and footage in manufacturing environments.

## Build/Test/Development Commands

### Running the Application
```bash
# Main entry point - prompts for interface choice
python OpToolKit.py

# Direct GUI launch
python OpToolKit.py --gui

# Direct console launch
python OpToolKit.py --console

# Console only (fallback)
python Menu.py
```

### Testing
This project uses manual testing. To test functionality:
1. Run the application using the commands above
2. Test both GUI and console interfaces
3. Verify calculations with known inputs/outputs

### Linting/Formatting
No formal linting configuration found. Follow the existing code style patterns observed in the codebase.

## Code Style Guidelines

### File Structure and Organization
- Main entry point: `OpToolKit.py` - handles CLI arguments and mode selection
- GUI interface: `gui.py` - contains `OperatorToolkitGUI` class
- Console interface: `Menu.py` - contains menu system
- Calculation modules: `Trimcalc.py`, `Partcalc.py`, `Footagecalc.py` - core calculation logic
- Each file should be self-contained with clear separation of concerns

### Import Style
```python
# Standard library imports first
import sys
import argparse

# Third-party imports next
import tkinter as tk
from tkinter import ttk, messagebox

# Local imports last
import Trimcalc
import Partcalc
import Footagecalc
```

### Naming Conventions
- **Files**: PascalCase for modules that match classes (`gui.py` contains `OperatorToolkitGUI`), otherwise lowercase (`Menu.py`, `Trimcalc.py`)
- **Classes**: PascalCase (`OperatorToolkitGUI`)
- **Functions/Methods**: snake_case (`main_menu`, `calculate_trim`, `mm_to_inches`)
- **Variables**: snake_case (`mr_size`, `slit_size_mm`, `num_slits`)
- **Constants**: Not extensively used, but follow UPPER_SNAKE_CASE if needed

### Function Documentation
```python
def function_name():
    """
    Brief description of what the function does.
    Additional details about the function's purpose or behavior.
    """
    # implementation
```

### Error Handling Patterns
- Use try-except blocks for user input validation
- Specific exception handling for ValueError on numeric inputs
- GUI: Use messagebox.showerror() for user feedback
- Console: Use print statements for error messages
- Graceful fallbacks (GUI to console mode)

### Code Formatting
- Indentation: 4 spaces (consistent throughout)
- Line length: Approximately 80-100 characters (existing code varies)
- Blank lines: Separate logical sections with blank lines
- Comments: Use docstrings for functions, minimal inline comments

### GUI Development Patterns
- Use tkinter with ttk themed widgets
- Class-based structure for GUI components
- Separate creation methods for each tab/section
- Use StringVar for input field binding
- Implement clear/reset functionality for each calculator
- Consistent padding and layout using grid/pack

### Console Development Patterns
- Menu-driven interface with numbered options
- Clear input prompts with expected units
- Input validation with user-friendly error messages
- Formatted output with 2 decimal places for calculations

### Calculation Logic
- Keep calculation logic separate from UI code
- Use helper functions for unit conversions (mm_to_inches)
- Perform calculations with appropriate data types (float vs int)
- Format results consistently (2 decimal places)
- Handle edge cases (division by zero, empty inputs)

### Adding New Features
1. Create new calculation module following the `Trimcalc.py`/`Partcalc.py`/`Footagecalc.py` pattern
2. Add corresponding GUI tab in `gui.py`
3. Add menu option in `Menu.py`
4. Update main application description if needed
5. Test both GUI and console interfaces

### Clear Calculator Feature
- **Module**: `Footagecalc.py` - calculates material length from roll dimensions
- **Formula**: Spiral length calculation: `π × (OuterRadius² - CoreRadius²) / MaterialThickness`
- **Units**: 
  - Diameters: Supports inches and millimeters with dropdown selection
  - Thickness: Uses "mill" (thousandths of an inch) only
- **Outputs**: Footage in feet and inches
- **Console**: Menu option 3, prompts for diameter units and measurements in mill for thickness
- **GUI**: Tab with dropdown for diameter units, mill-only thickness input, validation, and clear functionality
- **Validation**: Ensures positive values and core diameter < outer diameter
- **Helper Functions**: `mill_to_inches()` for thickness conversion

### Testing Approach
- Manual testing with known input/output pairs
- Test error conditions (invalid inputs, empty fields)
- Verify both GUI and console modes work correctly
- Test fallback mechanisms (GUI unavailable scenarios)

### Dependencies
- Python 3.x
- tkinter (standard library, but may need installation on some Linux systems)
- No external package management (pip, requirements.txt) currently used

### Git Configuration
- .gitignore excludes: __pycache__/, venv/, build/, dist/, image files
- No pre-commit hooks or automated formatting currently configured