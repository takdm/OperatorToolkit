def mm_to_inches(mm):
    """Convert millimeters to inches."""
    return mm / 25.4

def Trimcalc():
    """
    Perform trim calculation.
    This function simulates the trim calculation process.
    """
    print("Running Trimcalc...")
    try:
        mr_size = float(input("Enter MR Size (inches): "))
        slit_size_mm = float(input("Enter Slit Roll Size (mm): "))
        num_slits = int(input("Enter Number of Slits: "))
        roll_weight = float(input("Enter Label Roll Weight: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    slit_size_in = mm_to_inches(slit_size_mm)
    total_slit_width = slit_size_in * num_slits
    trim_size = mr_size - total_slit_width
    trim_weight = (roll_weight / slit_size_in) * trim_size if mr_size else 0

    print(f"\nTrim Size: {trim_size:.2f} inches")
    print(f"Trim Weight: {trim_weight:.2f}")