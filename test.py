from tkinter import *

# -------------------- CONSTANTS --------------------
FACTOR_MI_KM = 1.609344

# -------------------- STATE --------------------
mode = StringVar(value="IMP2MET")  # "IMP2MET" or "MET2IMP"

# -------------------- FUNCTIONS --------------------
def update_ui():
    """Refresh labels/placeholders according to current mode."""
    if mode.get() == "IMP2MET":
        input_unit_label.config(text="Miles")
        output_unit_label.config(text="Km")
        is_equal_label.config(text="Is equal to:")
    else:
        input_unit_label.config(text="Km")
        output_unit_label.config(text="Miles")
        is_equal_label.config(text="Is equal to:")
    # Do not clear user input automatically; just update result format
    # Optionally clear result when switching:
    result_label.config(text="0")

def set_mode_imp2met():
    mode.set("IMP2MET")
    update_ui()

def set_mode_met2imp():
    mode.set("MET2IMP")
    update_ui()

def show_help():
    top = Toplevel(window)
    top.title("Conversion Help")
    top.geometry("360x200")
    msg = (
        "Imperial → Metric: Miles → Kilometers (× 1.609344)\n"
        "Metric → Imperial: Kilometers → Miles (÷ 1.609344)\n\n"
        "Tips:\n"
        "• Left click Calculate or press Enter to convert.\n"
        "• Right click Calculate to clear.\n"
        "• Double left click Calculate to reset to 0."
    )
    Label(top, text=msg, justify="left").pack(padx=16, pady=16)

def convert(event=None):
    """Convert based on selected mode and update label."""
    try:
        value = float(input_entry.get())
        if mode.get() == "IMP2MET":
            out = value * FACTOR_MI_KM
        else:
            out = value / FACTOR_MI_KM
        result_label.config(text=f"{out:.2f}")
    except ValueError:
        result_label.config(text="Error")

def clear_input(event=None):
    input_entry.delete(0, END)
    result_label.config(text="0")

def reset_defaults(event=None):
    input_entry.delete(0, END)
    input_entry.insert(0, "0")
    result_label.config(text="0")

# -------------------- UI SETUP --------------------
window = Tk()
window.title("Miles ⇄ Kilometers Converter")
window.minsize(220, 220)
window.config(padx=50, pady=50)

# ----- Menu bar -----
menubar = Menu(window)
conversion_menu = Menu(menubar, tearoff=0)
conversion_menu.add_command(label="Imperial → Metric", command=set_mode_imp2met)
conversion_menu.add_command(label="Metric → Imperial", command=set_mode_met2imp)
conversion_menu.add_separator()
conversion_menu.add_command(label="Help…", command=show_help)
menubar.add_cascade(label="Conversion", menu=conversion_menu)
window.config(menu=menubar)

# ----- Mode Radios (top row) -----
modes_frame = Frame(window)
modes_frame.grid(column=0, row=0, columnspan=3, sticky="w", pady=(0, 10))
Radiobutton(modes_frame, text="Imperial → Metric", variable=mode, value="IMP2MET",
            command=update_ui).pack(side="left")
Radiobutton(modes_frame, text="Metric → Imperial", variable=mode, value="MET2IMP",
            command=update_ui).pack(side="left", padx=(12, 0))

# ----- Input row -----
input_entry = Entry(window, width=10, justify="right")
input_entry.grid(column=1, row=1)
input_entry.focus()

input_unit_label = Label(window, text="Miles")  # will update with mode
input_unit_label.grid(column=2, row=1)

# ----- Equals row -----
is_equal_label = Label(window, text="Is equal to:")
is_equal_label.grid(column=0, row=2)

result_label = Label(window, text="0")
result_label.grid(column=1, row=2)

output_unit_label = Label(window, text="Km")  # will update with mode
output_unit_label.grid(column=2, row=2)

# ----- Calculate button -----
calculate_button = Button(window, text="Calculate")
calculate_button.grid(column=1, row=3, pady=(10, 0))

# Binds (keep your behavior)
calculate_button.bind("<Button-1>", convert)               # Left click → convert
calculate_button.bind("<Button-3>", clear_input)           # Right click → clear
calculate_button.bind("<Double-Button-1>", reset_defaults) # Double left click → reset
window.bind("<Return>", convert)                           # Enter → convert

# Initialize labels to current mode
update_ui()

window.mainloop()
