import Trimcalc
import Partcalc
import Footagecalc

def main_menu():
    """
    Display the main menu and handle user input.
    Allows user to choose between running Trimcalc, PartCalc, Clearcalc, or exiting.
    """
    while True:
        print("\n=== Main Menu ===")
        print("1. Run setup calculator")
        print("2. Run partial calculator")
        print("3. Run clear calculator")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            Trimcalc.Trimcalc()
        elif choice == "2":
            Partcalc.Partcalc()
        elif choice == "3":
            Footagecalc.Clearcalc()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to execute the script
if __name__ == "__main__":
    # Display the main menu
    main_menu()
