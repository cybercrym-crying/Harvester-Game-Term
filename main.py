from entities.world_object import Cow, Animal, Chicken, show_animal
from entities.character import Player, createChar
from entities.item import ItemStack, listFoods
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen
from systems.time_system import TimeSystem
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


def make_start(player: Player):
    print("Hello {player.name}")


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


clock = TimeSystem()
print(clock.get_date())
if menu():
    MyPlayer = createChar()
    clear_screen()
    show_animal(list_player_animal)
else:
    pass
