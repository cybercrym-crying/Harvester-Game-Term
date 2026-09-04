from world_object import Cow, Animal, Chicken, show_animal
from character import Player, createChar
from item import ItemStack, listTools, listFoods
from InquirerPy import inquirer, prompts
from utility import clear_screen
import climage
import subprocess

list_player_animal = [
    Cow("Linda", "Female"),
    Cow("Murima", "Male"),
    Chicken("Merim", "Female"),
    Chicken("Rudi", "Male"),
]
list_player_animal[0].isAlive = False
list_player_animal[2].isAlive = False


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


if menu():
    MyPlayer = createChar()
    clear_screen()
    show_animal(list_player_animal)
else:
    pass
