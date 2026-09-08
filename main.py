from entities.animal_wo import Cow, Animal, Chicken, show_animal
from entities.character import Player, createChar
from entities.item import ItemStack
from entities.consumable_item import Food
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, wait_for_upscale_term, game_loading
from systems.time_system import TimeSystem
from core.enums import FoodType, RarityType
import climage
import subprocess
import time
from art import art, tprint

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


list_food = [
    Food("Rice", FoodType.GRAIN, RarityType.UNCOMMON),
    Food("White Onion", FoodType.FRUIT, RarityType.COMMON),
]
meal = Food("Fried Rice", FoodType.MEAL, recipe=[list_food[0], list_food[1]])
print(meal.get_info()["price"])
"""
tprint("HARVESTER", font="block")
time.sleep(5)
wait_for_upscale_term()
game_loading()
if menu():
    MyPlayer = createChar()
    clear_screen()
    show_animal(list_player_animal)
else:
    pass"""
