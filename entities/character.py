from systems.inventory_system import InventorySystem
from abc import ABC, abstractmethod
from datetime import date
from InquirerPy import inquirer, prompts
from utils.utility import clear_screen, validate_input
from core.enums import Effect


class Character(ABC):
    def __init__(self, name, gender, bornDate=date.today()):
        self.name = name
        self.__bornDate = bornDate
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\n"


class Player(Character):
    total_player = 0

    def __init__(self, name, gender, bornDate):
        super().__init__(name, gender, bornDate=date.today())
        Player.total_player += 1
        self.__gold = 100
        self.__stamina = 30
        self.__health = 50
        self.type_disease = None
        self.inventory = InventorySystem()

    def __str__(self):
        return (
            f"Name:   \t{self.name}\n"
            f"Gender: \t{self.gender}\n"
            f"Gold:   \t{self.__gold}\n"
            f"Stamina:\t{self.__stamina}\n"
            f"Health: \t{self.__health}\n"
            f"Disease \t{self.type_disease}\n"
        )

    def eat(self, consumable):
        from entities.consumable_item import Food, Medicine

        if Player not in consumable.target_entities:
            print(f"Cannot eat that thing...")
            return
        print(f"Eating {consumable.name}\n")
        if isinstance(consumable, Food):
            for k, v in consumable.effect.items():
                if k == Effect.HEAL:
                    self.health += v
                else:
                    self.stamina += v
        elif isinstance(consumable, Medicine):
            pass

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if not isinstance(value, (int, float)):
            print("Health must be integer")
            return
        self.__health = max(0, min(value, 100))

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not isinstance(value, (int, float)):
            print("Stamine must be integer")
            return
        self.__stamina = max(0, min(value, 100))

    @staticmethod
    def is_valid_name(name: str) -> bool:
        # helper validasi nama, gak butuh self/cls karena murni ngecek teks
        return (
            isinstance(name, str) and name.strip() != "" and not name.strip().isdigit()
        )

    @staticmethod
    def create_player():
        from data.item_data import list_tool, list_meal
        from entities.item import ItemStack, ItemCondition, Tools, WateringCane

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
