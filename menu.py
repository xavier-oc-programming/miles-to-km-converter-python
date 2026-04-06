import os
import subprocess
import sys
from pathlib import Path

from art import LOGO


def main() -> None:
    original = Path(__file__).parent / "original" / "mile_to_kilo_converter.py"
    advanced = Path(__file__).parent / "advanced" / "main.py"

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(LOGO)
        print("1. Original  – basic miles → km converter")
        print("2. Advanced  – bidirectional converter (OOP)")
        print("q. Quit")
        print()
        choice = input("Select: ").strip().lower()

        if choice == "1":
            subprocess.run([sys.executable, str(original)], cwd=str(original.parent))
        elif choice == "2":
            subprocess.run([sys.executable, str(advanced)], cwd=str(advanced.parent))
        elif choice == "q":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
