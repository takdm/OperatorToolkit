#!/usr/bin/env python3

import sys
import argparse
from Menu import main_menu

def main():
    """Main entry point that supports both GUI and console modes"""
    parser = argparse.ArgumentParser(description="Operator Toolkit - Manufacturing Calculator")
    parser.add_argument('--gui', action='store_true', 
                       help='Launch the GUI version (default: console)')
    parser.add_argument('--console', action='store_true', 
                       help='Launch the console version (default: console)')
    
    args = parser.parse_args()
    
    # If no arguments provided, check if GUI is available and ask user
    if not args.gui and not args.console and len(sys.argv) == 1:
        try:
            import tkinter
            print("Operator Toolkit")
            print("================")
            print("Choose interface:")
            print("1. GUI (Graphical User Interface)")
            print("2. Console (Text-based)")
            choice = input("Select an option (1 or 2): ").strip()
            
            if choice == "1":
                args.gui = True
            else:
                args.console = True
                
        except ImportError:
            print("GUI not available, using console mode...")
            args.console = True
    
    # Launch GUI mode
    if args.gui:
        try:
            import tkinter as tk
            from gui import OperatorToolkitGUI
            
            root = tk.Tk()
            app = OperatorToolkitGUI(root)
            root.mainloop()
            
        except ImportError:
            print("Error: GUI libraries not available. Please install tkinter.")
            print("Falling back to console mode...")
            main_menu()
        except Exception as e:
            print(f"Error launching GUI: {e}")
            print("Falling back to console mode...")
            main_menu()
    
    # Launch console mode (default)
    else:
        main_menu()


if __name__ == "__main__":
    main()