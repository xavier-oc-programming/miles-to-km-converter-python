# Miles ⇄ Km Converter

A Tkinter GUI that converts between miles and kilometers in both directions.

---

## Table of Contents

1. [Quick Start](#1-quick-start)
2. [Builds Comparison](#2-builds-comparison)
3. [Controls](#3-controls)
4. [App Flow](#4-app-flow)
5. [Features](#5-features)
6. [Navigation Flow](#6-navigation-flow)
7. [Architecture](#7-architecture)
8. [Module Reference](#8-module-reference)
9. [Configuration Reference](#9-configuration-reference)
10. [Display Layout](#10-display-layout)
11. [Design Decisions](#11-design-decisions)
12. [Course Context](#12-course-context)
13. [Dependencies](#13-dependencies)

---

## 1. Quick Start

```
python menu.py        # launcher — pick a build, or q to quit
python original/mile_to_kilo_converter.py   # run original directly
python advanced/main.py                     # run advanced directly
```

---

## 2. Builds Comparison

| Feature | Original | Advanced |
|---|---|---|
| Miles → Km conversion | ✓ | ✓ |
| Km → Miles conversion | — | ✓ |
| Mode toggle (radio buttons) | — | ✓ |
| Menu bar with Help dialog | — | ✓ |
| Enter key to convert | ✓ | ✓ |
| Right-click to clear | ✓ | ✓ |
| Double-click to reset to 0 | ✓ | ✓ |
| OOP architecture | — | ✓ |
| Config constants | — | ✓ |
| Pure-logic converter class | — | ✓ |

---

## 3. Controls

Both builds share the same button interaction model:

| Action | Trigger |
|---|---|
| Convert | Left click Calculate **or** press Enter |
| Clear input + result | Right click Calculate |
| Reset to 0 | Double left click Calculate |

**Advanced only — mode selection:**

| Action | Trigger |
|---|---|
| Switch to Imperial → Metric | Radio button or Conversion menu |
| Switch to Metric → Imperial | Radio button or Conversion menu |
| Open Help dialog | Conversion → Help… |

---

## 4. App Flow

1. Launch via `menu.py` (or directly).
2. The window opens with **Imperial → Metric** mode active.
3. Type a number into the entry field.
4. Click Calculate (or press Enter) — the result appears on the same row.
5. Right-click Calculate to clear; double-click to reset entry to `0`.
6. *(Advanced)* Use radio buttons or the menu bar to switch direction. The result clears automatically on mode change.
7. Close the window to exit.

---

## 5. Features

**Both builds**

**One-click conversion** — left click or Enter converts immediately; no separate "submit" step.

**Mouse shortcuts** — right-click clears the field and result; double-click resets the entry to `0` without clearing the result label style.

**Error handling** — entering non-numeric text shows `Error` instead of crashing.

**Advanced only**

**Bidirectional conversion** — toggle between Miles → Km and Km → Miles using radio buttons at the top of the window or the Conversion menu bar.

**Menu bar** — a native OS menu bar provides mode switching and a Help dialog explaining both directions and all mouse shortcuts.

**OOP architecture** — conversion logic lives in `Converter`, all rendering in `Display`, and `main.py` wires them together via callbacks. No function touches both logic and UI.

**Config module** — every constant (conversion factor, window dimensions, mode strings) is defined once in `config.py`; zero magic numbers elsewhere.

---

## 6. Navigation Flow

### a) Terminal menu tree

```
python menu.py
│
├── 1 ──► original/mile_to_kilo_converter.py  (subprocess)
│         [window opens → user closes → menu reappears]
│
├── 2 ──► advanced/main.py  (subprocess)
│         [window opens → user closes → menu reappears]
│
└── q ──► exit launcher
```

### b) In-app flow (advanced)

```
┌─────────────────────────────────────┐
│           Window opens              │
│     Mode: Imperial → Metric         │
└──────────────────┬──────────────────┘
                   │
        ┌──────────▼──────────┐
        │   Awaiting input    │◄──────────────────────┐
        └──────────┬──────────┘                       │
                   │                                  │
      ┌────────────┼────────────┐                     │
      │            │            │                     │
  Left click   Right click  Double click              │
  / Enter      Calculate    Calculate                 │
      │            │            │                     │
      ▼            ▼            ▼                     │
  Convert       Clear        Reset                    │
  → show        entry +      entry                    │
  result        result       to "0"                   │
      │            │            │                     │
      └────────────┴────────────┘                     │
                   │                                  │
          Radio / menu change                         │
                   │                                  │
                   ▼                                  │
           Flip mode labels                           │
           Clear entry + result ──────────────────────┘
```

---

## 7. Architecture

```
miles-to-km-converter-python/
│
├── menu.py          # launcher: prints LOGO, while-True menu, subprocess.run
├── art.py           # LOGO constant (ASCII art)
├── requirements.txt # stdlib only; Python 3.10+ note
├── .gitignore
├── README.md
│
├── docs/
│   └── COURSE_NOTES.md   # original exercise description and concepts
│
├── original/
│   └── mile_to_kilo_converter.py   # verbatim course file
│
└── advanced/
    ├── config.py      # every constant; zero magic numbers elsewhere
    ├── converter.py   # Converter class — pure logic, no tkinter
    ├── display.py     # Display class — owns root window and all widgets
    └── main.py        # orchestrator: instantiates classes, wires callbacks
```

---

## 8. Module Reference

### `Converter` (advanced/converter.py)

| Method | Returns | Description |
|---|---|---|
| `miles_to_km(miles)` | `float` | Multiply miles by `FACTOR_MI_KM` |
| `km_to_miles(km)` | `float` | Divide km by `FACTOR_MI_KM` |
| `convert(value, mode)` | `float` | Dispatch to the correct method based on mode constant |

### `Display` (advanced/display.py)

| Method | Returns | Description |
|---|---|---|
| `get_input()` | `str` | Raw text from the Entry widget |
| `get_mode()` | `str` | Current mode constant from the StringVar |
| `render_result(text)` | `None` | Set the result Label text |
| `render_units(input_unit, output_unit)` | `None` | Update both unit Labels |
| `clear()` | `None` | Delete entry content, reset result to `"0"` |
| `reset()` | `None` | Set entry to `"0"`, reset result to `"0"` |
| `show_help()` | `None` | Open a Toplevel help dialog |
| `close()` | `None` | `sys.exit(0)` |

---

## 9. Configuration Reference

All constants are in [advanced/config.py](advanced/config.py).

| Constant | Default | Description |
|---|---|---|
| `WINDOW_TITLE` | `"Miles ⇄ Km Converter"` | Root window title |
| `WINDOW_MIN_WIDTH` | `220` | Minimum window width (px) |
| `WINDOW_MIN_HEIGHT` | `220` | Minimum window height (px) |
| `WINDOW_PAD_X` | `50` | Horizontal padding inside the window |
| `WINDOW_PAD_Y` | `50` | Vertical padding inside the window |
| `FACTOR_MI_KM` | `1.609344` | Exact miles-to-km conversion factor |
| `MODE_IMP2MET` | `"IMP2MET"` | Mode string for Imperial → Metric |
| `MODE_MET2IMP` | `"MET2IMP"` | Mode string for Metric → Imperial |
| `ENTRY_WIDTH` | `10` | Character width of the Entry widget |
| `HELP_WINDOW_WIDTH` | `360` | Help Toplevel width (px) |
| `HELP_WINDOW_HEIGHT` | `200` | Help Toplevel height (px) |
| `RESULT_DEFAULT` | `"0"` | Text shown before first conversion |

---

## 10. Display Layout

```
┌──────────────────────────────────────────────────┐
│  Conversion ▾                    [menu bar]       │
├──────────────────────────────────────────────────┤
│  padx=50                                         │
│                                                  │
│  (●) Imperial → Metric  ( ) Metric → Imperial    │  row 0
│                                                  │
│                  [ 3.00  ]   Miles                │  row 1
│                                                  │
│  Is equal to:    [ 4.83  ]   Km                  │  row 2
│                                                  │
│                 [Calculate]                       │  row 3
│                                                  │
│  padx=50                                         │
└──────────────────────────────────────────────────┘
  col 0            col 1        col 2
```

---

## 11. Design Decisions

**`display.py` owns all UI** — conversion logic in `Converter` has no tkinter dependency. This makes `Converter` independently testable and lets you swap the GUI layer without touching the maths.

**`config.py` — zero magic numbers** — `1.609344`, `220`, `"IMP2MET"` each appear exactly once. Changing the window size or conversion factor is a single-line edit.

**`sys.path.insert` in `main.py`** — inserting `Path(__file__).parent` at the front of `sys.path` lets sibling imports (`from converter import Converter`) resolve correctly whether the file is launched by `menu.py` (via subprocess with `cwd=advanced/`) or run directly from any working directory.

**`subprocess.run` + `cwd=`** — the launcher passes `cwd=path.parent` so that Python's working directory matches the script's folder. Without this, relative imports inside the subprocess would fail when the menu is run from the repo root.

**`while True` in `menu.py` vs recursion** — calling `main()` from within itself would grow the call stack on every menu return. A plain loop is flat, has no stack growth, and exits cleanly on `break`.

**Console cleared before every menu render** — prevents stale output from a previous build's print statements bleeding into the menu display.

**`sys.exit(0)` in `Display.close()`** — calling only `root.destroy()` in a subprocess context can raise tkinter cleanup errors after the window closes. `sys.exit(0)` terminates the process cleanly.

**Callbacks injected via `__init__`** — `Display` accepts `on_convert`, `on_clear`, `on_reset`, and `on_mode_change` as constructor arguments rather than calling methods on a controller object. This keeps `Display` decoupled from `main.py`'s internals.

**`current_mode` as a one-element list** — Python closures capture variables by reference, but rebinding a name inside a nested function creates a local. Wrapping the mode string in a list (`current_mode[0]`) lets the callbacks mutate shared state without `nonlocal`.

---

## 12. Course Context

Built as **Day 27** of *100 Days of Code* by Dr. Angela Yu.

**Concepts covered in the original build:** `tkinter` basics, `Tk()` root window, `Entry`, `Label`, `Button`, `.grid()` layout, `padx`/`pady`, reading Entry input with `.get()`, updating Label with `.config()`, `<Return>` key binding, mouse event binding, basic `try/except`.

**The advanced build extends into:** OOP with a pure-logic class, separation of UI from logic via the display pattern, dependency injection via callbacks, a constants module, `sys.path` manipulation for subprocess-safe imports.

See [docs/COURSE_NOTES.md](docs/COURSE_NOTES.md) for full concept breakdown.

---

## 13. Dependencies

| Module | Used in | Purpose |
|---|---|---|
| `tkinter` | `advanced/display.py`, `original/mile_to_kilo_converter.py` | GUI framework |
| `sys` | `menu.py`, `advanced/main.py`, `advanced/display.py` | `sys.executable`, `sys.path`, `sys.exit` |
| `subprocess` | `menu.py` | Launch builds as child processes |
| `os` | `menu.py` | `os.system` to clear the terminal |
| `pathlib.Path` | `menu.py`, `advanced/main.py` | Resolve file paths relative to script location |
| `typing.Callable` | `advanced/display.py` | Type hints for callback parameters |
