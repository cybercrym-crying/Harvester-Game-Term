from systems.inventory_system import InventorySystem
from data.item_data import Tools
from abc import ABC, abstractmethod
from entities.item import ItemStack, ItemCondition, Tools, WateringCane
from data.item_data import list_item, list_tool, list_meal
from datetime import date
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, validate_input


class Character(ABC):
    def __init__(self, name, gender, bornDate=date.today()):
        self.name = name
        self.__bornDate = bornDate
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\n"


class Player(Character):
    def __init__(self, name, gender, bornDate):
        super().__init__(name, gender, bornDate=date.today())
        self.gold = 100
        self.stamina = 50
        self.health = 100
        self.inventory = InventorySystem()

    @staticmethod
    def create_player():
        confirm = False
        while not confirm:
            name = inquirer.text(message="What's your name:").execute()
            if validate_input(name):
                gender = inquirer.select(
                    message="What's your Gender:",
                    choices=["Man", "Woman"],
                ).execute()
                confirm = inquirer.confirm(message="Confirm?").execute()
                if confirm:
                    player = Player(name, gender, date.today())
                    player.inventory.add_new_item(ItemStack(list_tool["Steel Axe"], 1))
                    player.inventory.add_new_item(ItemStack(list_tool["Steel Hoe"], 1))
                    player.inventory.add_new_item(
                        ItemStack(list_tool["Steel Shovel"], 1)
                    )
                    player.inventory.add_new_item(
                        ItemStack(list_tool["Steel Pickaxe"], 1)
                    )
                    player.inventory.add_new_item(
                        ItemStack(list_tool["Steel Sickle"], 1)
                    )
                    return Player(name, gender, date.today())
                else:
                    clear_screen()
                    continue
