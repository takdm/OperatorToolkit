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

def PartCalc():
    """
    Perform part calculation.
    This function simulates the part calculation process.
    """
    print("Running PartCalc...")
    # Prompt user for the full roll footage (in feet)
    print("Enter full roll footage:")
    fullfeet = int(input())

    # Prompt user for the full roll weight
    print("Enter full roll weight:")
    fullweight = int(input())

    # Prompt user for the partial roll footage (rounded, in feet)
    print("Enter partial footage (rounded):")
    partfootage = int(input())

    # Prompt user for the number of lanes
    print("Enter amount of lanes:")
    lanes = int(input())

    # Calculate the weight of the partial roll
    partialweight = fullweight / fullfeet * partfootage

    # Output the results
    print("Your per roll partial weight is", partialweight)
    print("Your partials total at", lanes * partialweight)

def main_menu():
    """
    Display the main menu and handle user input.
    Allows the user to choose between running Trimcalc, PartCalc, or exiting.
    """
    while True:
        print("\n=== Main Menu ===")
        print("1. Run Trimcalc")
        print("2. Run PartCalc")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            Trimcalc()
        elif choice == "2":
            PartCalc()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to execute the script
if __name__ == "__main__":
    # Display the main menu
    main_menu()
