from entities.character import *
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, wait_for_upscale_term, game_loading
import climage
import subprocess
import time
from art import art, tprint


def menu(player):
    m = f"Hellooo Player, Welcome to Harvester"
    confirm = inquirer.select(
        message=m,
        choices=["Start", "Exit"],
    ).execute()
    if confirm == "Start":
        player = createChar()
    else:
        exit(0)


my_player = None
tprint("HARVESTER", font="block")
time.sleep(5)
wait_for_upscale_term()
game_loading()
menu(my_player)
