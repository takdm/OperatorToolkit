def mm_to_inches(mm):
    """Convert millimeters to inches."""
    return mm / 25.4

def mill_to_inches(mill):
    """Convert thousandths of an inch to inches."""
    return mill / 1000

def inches_to_feet(inches):
    """Convert inches to feet."""
    return inches / 12

def validate_positive_input(value, field_name):
    """Validate that input is positive."""
    if value <= 0:
        raise ValueError(f"{field_name} must be positive")
    return value

def Clearcalc():
    """
    Calculate roll footage based on diameter measurements and material thickness.
    Supports inches/millimeters for diameters and mill (thousandths of inch) for thickness.
    """
    print("Running Clear Calculator...")
    
    try:
        # Unit selection for diameters
        print("Select units for diameters:")
        print("1. Inches")
        print("2. Millimeters")
        diameter_unit_choice = input("Select option (1 or 2): ")
        
        if diameter_unit_choice not in ["1", "2"]:
            print("Invalid choice. Please select 1 or 2.")
            return
        
        # Get diameter inputs
        if diameter_unit_choice == "1":
            outer_diameter = float(input("Enter roll outer diameter (inches): "))
            core_diameter = float(input("Enter core diameter (inches): "))
        else:
            outer_diameter = float(input("Enter roll outer diameter (mm): "))
            core_diameter = float(input("Enter core diameter (mm): "))
            # Convert to inches for calculation
            outer_diameter = mm_to_inches(outer_diameter)
            core_diameter = mm_to_inches(core_diameter)
        
        # Validate diameters
        validate_positive_input(outer_diameter, "Outer diameter")
        validate_positive_input(core_diameter, "Core diameter")
        
        if core_diameter >= outer_diameter:
            print("Error: Core diameter must be smaller than outer diameter.")
            return
        
        # Get material thickness input (always in mill)
        material_thickness_mill = float(input("Enter material thickness (mill): "))
        material_thickness = mill_to_inches(material_thickness_mill)
        
        # Validate material thickness
        validate_positive_input(material_thickness, "Material thickness")
        
        # Calculate footage using spiral length formula
        # Footage = π × (OuterRadius² - CoreRadius²) / MaterialThickness
        outer_radius = outer_diameter / 2
        core_radius = core_diameter / 2
        
        footage_inches = 3.14159 * (outer_radius**2 - core_radius**2) / material_thickness
        footage_feet = inches_to_feet(footage_inches)
        
        # Display results
        print(f"\n=== Results ===")
        print(f"Roll outer diameter: {outer_diameter:.2f} inches")
        print(f"Core diameter: {core_diameter:.2f} inches")
        print(f"Material thickness: {material_thickness_mill:.1f} mill ({material_thickness:.4f} inches)")
        print(f"Calculated Footage: {footage_feet:.2f} feet")
        
        # Additional useful calculations
        if diameter_unit_choice == "2":
            original_outer_mm = outer_diameter * 25.4
            original_core_mm = core_diameter * 25.4
            print(f"Original outer diameter: {original_outer_mm:.2f} mm")
            print(f"Original core diameter: {original_core_mm:.2f} mm")
        
    except ValueError as e:
        if "must be positive" in str(e):
            print(f"Error: {e}")
        else:
            print("Invalid input. Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")