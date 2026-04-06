# Course Notes — Day 27: Miles to Kilometer Converter

## Original Exercise

Build a GUI application using **tkinter** that converts miles to kilometers.

The exercise introduces tkinter's grid layout system and basic widget interaction.

## Concepts Covered

- `tkinter` — Python's built-in GUI toolkit
- `Tk()` — creating the root window
- `Entry` — single-line text input widget
- `Label` — text display widget
- `Button` — clickable button widget
- `.grid()` — placing widgets using row/column coordinates
- `window.config(padx=, pady=)` — adding padding around the window
- Reading user input with `.get()` on an Entry widget
- Updating a Label dynamically with `.config(text=...)`
- Binding keyboard events with `window.bind("<Return>", callback)`
- Binding mouse events with `.bind("<Button-1>", callback)`
- Basic exception handling (`try/except ValueError`) for invalid input

## Original Task Requirements

1. Create a window titled "Miles to Kilometers Converter"
2. Add an Entry field for the user to type a miles value
3. Add a "Miles" label next to the entry
4. Add an "Is equal to:" label on the left
5. Display the converted kilometer result in a label
6. Add a "Km" label next to the result
7. Add a "Calculate" button that triggers the conversion
8. Formula: `km = miles × 1.609344`

## Layout (Grid)

```
col 0           col 1         col 2
                [Entry]       Miles
Is equal to:    [Result]      Km
                [Calculate]
```
