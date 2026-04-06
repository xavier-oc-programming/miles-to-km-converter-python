import sys
from tkinter import END, Entry, Frame, Label, Menu, Radiobutton, Tk, Toplevel, Button, StringVar
from typing import Callable

from config import (
    ENTRY_WIDTH,
    HELP_WINDOW_HEIGHT,
    HELP_WINDOW_WIDTH,
    MODE_IMP2MET,
    MODE_MET2IMP,
    RESULT_DEFAULT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_PAD_X,
    WINDOW_PAD_Y,
    WINDOW_TITLE,
)


class Display:
    """Owns the Tk root window and every widget. No conversion logic lives here."""

    def __init__(
        self,
        on_convert: Callable[[], None],
        on_clear: Callable[[], None],
        on_reset: Callable[[], None],
        on_mode_change: Callable[[str], None],
    ) -> None:
        self._on_convert = on_convert
        self._on_clear = on_clear
        self._on_reset = on_reset
        self._on_mode_change = on_mode_change

        self.root = Tk()
        self.root.title(WINDOW_TITLE)
        self.root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        self.root.config(padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y)

        self._mode_var = StringVar(value=MODE_IMP2MET)
        self._build_menu()
        self._build_widgets()
        self.root.focus_set()

    # ---- private builders ----

    def _build_menu(self) -> None:
        menubar = Menu(self.root)
        conv_menu = Menu(menubar, tearoff=0)
        conv_menu.add_command(
            label="Imperial \u2192 Metric",
            command=lambda: self._handle_mode_change(MODE_IMP2MET),
        )
        conv_menu.add_command(
            label="Metric \u2192 Imperial",
            command=lambda: self._handle_mode_change(MODE_MET2IMP),
        )
        conv_menu.add_separator()
        conv_menu.add_command(label="Help\u2026", command=self.show_help)
        menubar.add_cascade(label="Conversion", menu=conv_menu)
        self.root.config(menu=menubar)

    def _build_widgets(self) -> None:
        # Mode radio buttons
        modes_frame = Frame(self.root)
        modes_frame.grid(column=0, row=0, columnspan=3, sticky="w", pady=(0, 10))
        Radiobutton(
            modes_frame,
            text="Imperial \u2192 Metric",
            variable=self._mode_var,
            value=MODE_IMP2MET,
            command=lambda: self._handle_mode_change(MODE_IMP2MET),
        ).pack(side="left")
        Radiobutton(
            modes_frame,
            text="Metric \u2192 Imperial",
            variable=self._mode_var,
            value=MODE_MET2IMP,
            command=lambda: self._handle_mode_change(MODE_MET2IMP),
        ).pack(side="left", padx=(12, 0))

        # Input row
        self._input_entry = Entry(self.root, width=ENTRY_WIDTH, justify="right")
        self._input_entry.grid(column=1, row=1)
        self._input_entry.focus()

        self._input_unit_label = Label(self.root, text="Miles")
        self._input_unit_label.grid(column=2, row=1)

        # Result row
        Label(self.root, text="Is equal to:").grid(column=0, row=2)
        self._result_label = Label(self.root, text=RESULT_DEFAULT)
        self._result_label.grid(column=1, row=2)
        self._output_unit_label = Label(self.root, text="Km")
        self._output_unit_label.grid(column=2, row=2)

        # Calculate button
        calc_btn = Button(self.root, text="Calculate")
        calc_btn.grid(column=1, row=3, pady=(10, 0))
        calc_btn.bind("<Button-1>", lambda e: self._on_convert())
        calc_btn.bind("<Button-3>", lambda e: self._on_clear())
        calc_btn.bind("<Double-Button-1>", lambda e: self._on_reset())
        self.root.bind("<Return>", lambda e: self._on_convert())

    def _handle_mode_change(self, mode: str) -> None:
        self._mode_var.set(mode)
        self._on_mode_change(mode)

    # ---- public ----

    def get_input(self) -> str:
        return self._input_entry.get()

    def get_mode(self) -> str:
        return self._mode_var.get()

    def render_result(self, text: str) -> None:
        self._result_label.config(text=text)

    def render_units(self, input_unit: str, output_unit: str) -> None:
        self._input_unit_label.config(text=input_unit)
        self._output_unit_label.config(text=output_unit)

    def clear(self) -> None:
        self._input_entry.delete(0, END)
        self._result_label.config(text=RESULT_DEFAULT)

    def reset(self) -> None:
        self._input_entry.delete(0, END)
        self._input_entry.insert(0, "0")
        self._result_label.config(text=RESULT_DEFAULT)

    def show_help(self) -> None:
        top = Toplevel(self.root)
        top.title("Conversion Help")
        top.geometry(f"{HELP_WINDOW_WIDTH}x{HELP_WINDOW_HEIGHT}")
        msg = (
            "Imperial \u2192 Metric: Miles \u2192 Kilometers (\u00d7 1.609344)\n"
            "Metric \u2192 Imperial: Kilometers \u2192 Miles (\u00f7 1.609344)\n\n"
            "Tips:\n"
            "\u2022 Left click Calculate or press Enter to convert.\n"
            "\u2022 Right click Calculate to clear.\n"
            "\u2022 Double left click Calculate to reset to 0."
        )
        Label(top, text=msg, justify="left").pack(padx=16, pady=16)

    def close(self) -> None:
        sys.exit(0)
