import os
import re
import shutil
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def check_term_size():
    width = shutil.get_terminal_size().columns
    high = shutil.get_terminal_size().lines
    return width * high


def wait_for_upscale_term():
    req_term_size = 5400
    curr_term_size = check_term_size()
    last_size = None
    while curr_term_size < req_term_size:
        com_term_size = check_term_size()
        if last_size != curr_term_size:
            print(f"Terminal Size to small: {curr_term_size}")
            print("Up your terminal size first")
            last_size = curr_term_size
        curr_term_size = check_term_size()
        time.sleep(1)
        clear_screen()


def validate_input(input):
    clear_input = input.strip()
    check_symbol = bool(re.search(r"[^a-zA-Z0-9\s]", clear_input))
    if clear_input.isdigit() or len(clear_input) == 0 or check_symbol:
        return False
    else:
        return True


def game_loading():
    text = "LOADING...."
    line_animation = ["|", "/", "-", "\\", "|", "/", "-", "\\"]
    for j in range(0, 3):
        clear_screen()
        for i in range(0, len(line_animation), 1):
            print(text + "[ " + line_animation[i] + " ]")
            time.sleep(0.2)
            clear_screen()
