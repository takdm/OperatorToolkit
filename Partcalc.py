def Partcalc():
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

    # Output the results with floats to 2 decimal places
    print("Your per roll partial weight is {:.2f}".format(partialweight))
    print("Your partials total at {:.2f}".format(lanes * partialweight))
