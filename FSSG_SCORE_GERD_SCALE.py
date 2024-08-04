Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import ttk


def calculate_total():
    total = sum(int(option_to_value[entry.get()]) for entry in dropdowns)
    total_label.config(text=f"Total: {total}")


def determine_gerd():
    fssg_score = sum(int(option_to_value[entry.get()]) for entry in dropdowns)

    if fssg_score >= 0 and fssg_score <= 7:
        result = "No GERD"
    elif fssg_score == 8:
        result = "GERD"
    elif fssg_score >= 9 and fssg_score <= 18:
        result = "GERD1"
    elif fssg_score >= 19 and fssg_score <= 28:
        result = "GERD2"
    elif fssg_score >= 29 and fssg_score <= 38:
        result = "GERD3"
...     elif fssg_score >= 39 and fssg_score <= 48:
...         result = "GERD4"
...     else:
...         result = "Invalid FSSG score"
... 
...     result_label.config(text=f"The patient's GERD level is: {result}")
... 
... 
... # Create the main window
... root = tk.Tk()
... root.title("FSSG Score and GERD Diagnosis Tool")
... root.configure(bg="#4287f5")
... 
... # Create labels and dropdown menus
... option_to_value = {
...     "Never": 0,
...     "Occasionally": 1,
...     "Sometimes": 2,
...     "Often": 3,
...     "Always": 4
... }
... 
... labels = [
...     tk.Label(root, text="Q1 Do you get heartburn?", font=("Arial", 12)),
...     tk.Label(root, text="Q2 Does your stomach get bloated?", font = ("Arial", 12)),
...     tk.Label(root, text="Q3 Does your stomach ever feel heavy after meals?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q4 Do you sometimes subconsciously rub your chest with your hand?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q5 Do you ever feel sick after meals?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q6 Do you get heartburn after meals?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q7 Do you have an unusual (eg, burning) sensation in your throat?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q8 Do you feel full while eating meals?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q9 Do some things get stuck when you swallow?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q10 Do you get bitter liquid (acid) coming up into your throat?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q11 Do you burp a lot?" , font = ("Arial", 12)),
...     tk.Label(root, text="Q12 Do you get heartburn if you bend over?" , font = ("Arial", 12)) ,
... ]
... 
... dropdowns = [ttk.Combobox(root, values=list(option_to_value.keys()), state="readonly", font=("Arial", 12)) for _ in
...              range(12)]
... 
... # Add labels and dropdown menus to the main window
... for i in range(12):
...     labels[i].grid(row=i, column=0, sticky="w", padx=10, pady=5)
...     dropdowns[i].grid(row=i, column=1, padx=10, pady=5)
... 
... # Create the "Calculate FSSG Score" button
... button_calculate_total = tk.Button(root, text="Calculate FSSG Score", font=("Arial", 12, "bold"),
                                   command=calculate_total)
button_calculate_total.grid(row=13, column=0, columnspan=2, pady=15)

# Create a label to display the total FSSG score
total_label = tk.Label(root, text="Total: 0", font=("Arial", 14, "bold"))
total_label.grid(row=14, column=0, columnspan=2)

# Create a button to determine GERD level and display the result
button_determine_gerd = tk.Button(root, text="Determine GERD Level", font=("Arial", 12, "bold"), command=determine_gerd)
button_determine_gerd.grid(row=15, column=0, columnspan=2, pady=15)

# Create a label to display the GERD diagnosis result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=16, column=0, columnspan=2, pady=10)

# Developer information label
developer_label = tk.Label(root, text="Developed by KRISHNA SAHA , M.SC IT (DATA SCIENCE) from MAKAUT.WB",
                           font=("Arial", 10))
developer_label.grid(row=17, column=0, columnspan=2, pady=5)

# Start the main loop
root.mainloop()
[DEBUG ON]
[DEBUG OFF]
