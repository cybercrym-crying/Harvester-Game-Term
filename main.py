from entities.character import Player
from data.item_data import list_food, list_meal, list_herb
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, wait_for_upscale_term, game_loading
import climage
import subprocess
import time
from art import art, tprint
from entities.animal_wo import Cow


def menu():
    """
    tprint("HARVESTER", font="block")
    time.sleep(5)
    wait_for_upscale_term()
    game_loading()
    """
    m = f"Hellooo Player, Welcome to Harvester"
    confirm = inquirer.select(
        message=m,
        choices=["Start", "Exit"],
    ).execute()
    if confirm == "Start":
        return Player.create_player()
    else:
        exit(0)


data_sapi = {
    "name": "Moli",
    "gender": "Female",
    "health": 80,
}  # anggap sebagai data dari file
sapi_baru = Cow.from_dict(data_sapi)
my_player = menu()
print(my_player)
print(list_food["Rice"])
print(sapi_baru)
if my_player:
    pass
