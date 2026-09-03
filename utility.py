import os
import re


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def validate_input(input):
    clear_input = input.strip()
    check_symbol = bool(re.search(r"[^a-zA-Z0-9\s]", clear_input))
    if clear_input.isdigit() or len(clear_input) == 0 or check_symbol:
        return False
    else:
        return True
