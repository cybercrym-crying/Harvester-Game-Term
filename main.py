from entities.animal import Cow, Animal, Chicken, show_animal
from entities.character import Player, createChar
from entities.item import ItemStack, listFoods
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, wait_for_upscale_term, game_loading
from systems.time_system import TimeSystem
import climage
import subprocess
import time

list_player_animal = [
    Cow("Linda", "Female"),
    Cow("Linda", "Female"),
    Cow("Linda", "Female"),
    Cow("Murima", "Male"),
    Chicken("Merim", "Female"),
    Cow("Murima", "Male"),
    Chicken("Merim", "Female"),
    Chicken("Merim", "Female"),
    Chicken("Rudi", "Male"),
    Chicken("Rudi", "Male"),
]
list_player_animal[0].is_alive = False


def menu():
    m = f"Hellooo Player, Welcome to Harvester"
    confirm = inquirer.select(
        message=m,
        choices=["Start", "Exit"],
    ).execute()
    if confirm == "Start":
        return True
    else:
        exit(0)


wait_for_upscale_term()
game_loading()
if menu():
    MyPlayer = createChar()
    clear_screen()
    show_animal(list_player_animal)
else:
    pass
