import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import MODE_IMP2MET, MODE_MET2IMP
from converter import Converter
from display import Display


def main() -> None:
    converter = Converter()
    current_mode: list[str] = [MODE_IMP2MET]  # list used as mutable closure cell

    def on_convert() -> None:
        raw = display.get_input()
        try:
            value = float(raw)
            result = converter.convert(value, current_mode[0])
            display.render_result(f"{result:.2f}")
        except ValueError:
            display.render_result("Error")

    def on_clear() -> None:
        display.clear()

    def on_reset() -> None:
        display.reset()

    def on_mode_change(mode: str) -> None:
        current_mode[0] = mode
        if mode == MODE_IMP2MET:
            display.render_units("Miles", "Km")
        else:
            display.render_units("Km", "Miles")
        display.clear()

    display = Display(
        on_convert=on_convert,
        on_clear=on_clear,
        on_reset=on_reset,
        on_mode_change=on_mode_change,
    )

    display.root.mainloop()


if __name__ == "__main__":
    main()
