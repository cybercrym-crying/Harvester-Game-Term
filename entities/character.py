from systems.inventory_system import InventorySystem
from abc import ABC, abstractmethod
from entities.item import Food, ItemCondition, Tools
from datetime import date
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, validate_input


class Character(ABC):
    def __init__(self, name, gender, bornDate=date.today()):
        self.name = name
        self.__bornDate = bornDate
        self.gender = gender
        self.inventory = InventorySystem()

    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\n"


class Player(Character):
    def __init__(self, name, gender, bornDate):
        super().__init__(name, gender, bornDate=date.today())
        self.gold = 100
        self.strength = 100
        self.stamina = 100

    def eating(self, food: Food):
        if food.condition == ItemCondition.GOOD.name and self.stamina < 100:
            if food.calorie <= (100 - self.stamina):
                self.stamina += food.calorie
            else:
                self.stamina += food.calorie - (food.calorie - (100 - self.stamina))
                food.calorie -= 100 - self.stamina


def createChar():
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
                return Player(name, gender, date.today())
            else:
                clear_screen()
                continue
