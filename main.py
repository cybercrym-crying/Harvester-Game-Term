from entities.character import Player
from data.item_data import list_food, list_meal
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, wait_for_upscale_term, game_loading
import climage
import subprocess
import time
from art import art, tprint


def menu():
    m = f"Hellooo Player, Welcome to Harvester"
    confirm = inquirer.select(
        message=m,
        choices=["Start", "Exit"],
    ).execute()
    if confirm == "Start":
        return Player.create_player()
    else:
        exit(0)


my_player = menu()
tprint("HARVESTER", font="block")
time.sleep(5)
wait_for_upscale_term()
game_loading()
print(list_food["Rice"])
print(list_meal[2])
print(list_meal[3])
print(my_player)
if my_player:
    my_player.eat(list_food["Rice"])
print(my_player)
