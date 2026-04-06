from tkinter import *

# -------------------- FUNCTIONS --------------------
def miles_to_km(event=None):
    """Convert miles to kilometers and update label."""
    try:
        miles = float(miles_input.get())
        kilometers = 1.609344 * miles
        kilometer_results_label.config(text=f"{kilometers:.2f}")
    except ValueError:
        kilometer_results_label.config(text="Error")

def clear_input(event=None):
    """Clear the miles entry and result label."""
    miles_input.delete(0, END)
    kilometer_results_label.config(text="0")



# -------------------- UI SETUP --------------------
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(150, 200)
window.config(padx=50, pady=50)

# ---Miles----
miles_input = Entry(width=10, justify="right")
miles_input.grid(column=1, row=0)
miles_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# ---Is equal to----
is_equal_label = Label(text="Is equal to:")
is_equal_label.grid(column=0, row=1)

kilometer_results_label = Label(text="0")
kilometer_results_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# ---Calculate button---
calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)

# Bind mouse events
calculate_button.bind("<Button-1>", miles_to_km)          # Left click → calculate
calculate_button.bind("<Button-2>", clear_input)          # Right click → clear
calculate_button.bind("<Double-Button-1>", clear_input)   # Doubke left click → clear

# Optional: press Enter anywhere to calculate
window.bind("<Return>", miles_to_km)

window.mainloop()
