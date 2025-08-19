#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
import Trimcalc
import Partcalc

class OperatorToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Operator Toolkit")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create main menu tab
        self.create_main_menu()
        
        # Create Trimcalc tab
        self.create_trimcalc_tab()
        
        # Create Partcalc tab
        self.create_partcalc_tab()

    def create_main_menu(self):
        """Create the main menu tab"""
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="Main Menu")
        
        # Title
        title_label = ttk.Label(main_frame, text="Operator Toolkit", font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Description
        desc_label = ttk.Label(main_frame, 
                              text="Choose a calculator from the tabs above or use the buttons below:",
                              font=('Arial', 10))
        desc_label.pack(pady=10)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=20)
        
        # Buttons
        trimcalc_btn = ttk.Button(buttons_frame, text="Setup Calculator (Trimcalc)", 
                                 command=lambda: self.notebook.select(1), width=25)
        trimcalc_btn.pack(pady=10)
        
        partcalc_btn = ttk.Button(buttons_frame, text="Partial Calculator (Partcalc)", 
                                 command=lambda: self.notebook.select(2), width=25)
        partcalc_btn.pack(pady=10)

    def create_trimcalc_tab(self):
        """Create the Trimcalc tab"""
        trim_frame = ttk.Frame(self.notebook)
        self.notebook.add(trim_frame, text="Setup Calculator")
        
        # Title
        title_label = ttk.Label(trim_frame, text="Setup Calculator (Trimcalc)", font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = ttk.LabelFrame(trim_frame, text="Input Parameters", padding=10)
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # MR Size
        ttk.Label(input_frame, text="MR Size (inches):").grid(row=0, column=0, sticky='w', pady=5)
        self.mr_size_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.mr_size_var, width=20).grid(row=0, column=1, pady=5, padx=10)
        
        # Slit Roll Size
        ttk.Label(input_frame, text="Slit Roll Size (mm):").grid(row=1, column=0, sticky='w', pady=5)
        self.slit_size_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.slit_size_var, width=20).grid(row=1, column=1, pady=5, padx=10)
        
        # Number of Slits
        ttk.Label(input_frame, text="Number of Slits:").grid(row=2, column=0, sticky='w', pady=5)
        self.num_slits_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.num_slits_var, width=20).grid(row=2, column=1, pady=5, padx=10)
        
        # Label Roll Weight
        ttk.Label(input_frame, text="Label Roll Weight:").grid(row=3, column=0, sticky='w', pady=5)
        self.roll_weight_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.roll_weight_var, width=20).grid(row=3, column=1, pady=5, padx=10)
        
        # Calculate button
        calc_btn = ttk.Button(trim_frame, text="Calculate", command=self.calculate_trim, width=15)
        calc_btn.pack(pady=10)
        
        # Results frame
        results_frame = ttk.LabelFrame(trim_frame, text="Results", padding=10)
        results_frame.pack(fill='x', padx=20, pady=10)
        
        self.trim_results = tk.Text(results_frame, height=4, width=50)
        self.trim_results.pack(fill='x')
        
        # Clear button
        clear_btn = ttk.Button(trim_frame, text="Clear", command=self.clear_trim, width=15)
        clear_btn.pack(pady=5)

    def create_partcalc_tab(self):
        """Create the Partcalc tab"""
        part_frame = ttk.Frame(self.notebook)
        self.notebook.add(part_frame, text="Partial Calculator")
        
        # Title
        title_label = ttk.Label(part_frame, text="Partial Calculator (Partcalc)", font=('Arial', 14, 'bold'))
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = ttk.LabelFrame(part_frame, text="Input Parameters", padding=10)
        input_frame.pack(fill='x', padx=20, pady=10)
        
        # Full roll footage
        ttk.Label(input_frame, text="Full Roll Footage:").grid(row=0, column=0, sticky='w', pady=5)
        self.full_feet_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.full_feet_var, width=20).grid(row=0, column=1, pady=5, padx=10)
        
        # Full roll weight
        ttk.Label(input_frame, text="Full Roll Weight:").grid(row=1, column=0, sticky='w', pady=5)
        self.full_weight_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.full_weight_var, width=20).grid(row=1, column=1, pady=5, padx=10)
        
        # Partial footage
        ttk.Label(input_frame, text="Partial Footage (rounded):").grid(row=2, column=0, sticky='w', pady=5)
        self.part_footage_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.part_footage_var, width=20).grid(row=2, column=1, pady=5, padx=10)
        
        # Number of lanes
        ttk.Label(input_frame, text="Number of Lanes:").grid(row=3, column=0, sticky='w', pady=5)
        self.lanes_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.lanes_var, width=20).grid(row=3, column=1, pady=5, padx=10)
        
        # Full trim weight
        ttk.Label(input_frame, text="Full Trim Weight:").grid(row=4, column=0, sticky='w', pady=5)
        self.full_trim_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.full_trim_var, width=20).grid(row=4, column=1, pady=5, padx=10)
        
        # Calculate button
        calc_btn = ttk.Button(part_frame, text="Calculate", command=self.calculate_part, width=15)
        calc_btn.pack(pady=10)
        
        # Results frame
        results_frame = ttk.LabelFrame(part_frame, text="Results", padding=10)
        results_frame.pack(fill='x', padx=20, pady=10)
        
        self.part_results = tk.Text(results_frame, height=8, width=50)
        self.part_results.pack(fill='x')
        
        # Clear button
        clear_btn = ttk.Button(part_frame, text="Clear", command=self.clear_part, width=15)
        clear_btn.pack(pady=5)

    def calculate_trim(self):
        """Calculate trim using the same logic as Trimcalc module"""
        try:
            # Get inputs
            mr_size = float(self.mr_size_var.get())
            slit_size_mm = float(self.slit_size_var.get())
            num_slits = int(self.num_slits_var.get())
            roll_weight = float(self.roll_weight_var.get())
            
            # Use the same calculation logic from Trimcalc module
            slit_size_in = Trimcalc.mm_to_inches(slit_size_mm)
            total_slit_width = slit_size_in * num_slits
            trim_size = mr_size - total_slit_width
            trim_weight = (roll_weight / slit_size_in) * trim_size if mr_size else 0
            
            # Display results
            results = f"Trim Size: {trim_size:.2f} inches\n"
            results += f"Trim Weight: {trim_weight:.2f}"
            
            self.trim_results.delete(1.0, tk.END)
            self.trim_results.insert(1.0, results)
            
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def calculate_part(self):
        """Calculate partial using the same logic as Partcalc module"""
        try:
            # Get inputs
            fullfeet = int(self.full_feet_var.get())
            fullweight = int(self.full_weight_var.get())
            partfootage = int(self.part_footage_var.get())
            lanes = int(self.lanes_var.get())
            fulltrim = int(self.full_trim_var.get())
            
            # Use the same calculation logic from Partcalc module
            partialweight = fullweight / fullfeet * partfootage
            partialtrim = fulltrim / fullfeet * partfootage
            reroll = fullweight - partialweight
            reset = reroll * lanes
            retrim = fulltrim - partialtrim
            
            # Display results
            results = f"Your per roll partial weight is {partialweight:.2f}\n"
            results += f"Your partials total at {lanes * partialweight:.2f}\n"
            results += f"Your partial trim weight is {partialtrim:.2f}\n"
            results += f"Your remaining rolls weight is {reroll:.2f}\n"
            results += f"Your remaining set weight is {reset:.2f}\n"
            results += f"Your remaining trim weight is {retrim:.2f}"
            
            self.part_results.delete(1.0, tk.END)
            self.part_results.insert(1.0, results)
            
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_trim(self):
        """Clear all Trimcalc inputs and results"""
        self.mr_size_var.set("")
        self.slit_size_var.set("")
        self.num_slits_var.set("")
        self.roll_weight_var.set("")
        self.trim_results.delete(1.0, tk.END)

    def clear_part(self):
        """Clear all Partcalc inputs and results"""
        self.full_feet_var.set("")
        self.full_weight_var.set("")
        self.part_footage_var.set("")
        self.lanes_var.set("")
        self.full_trim_var.set("")
        self.part_results.delete(1.0, tk.END)


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = OperatorToolkitGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()