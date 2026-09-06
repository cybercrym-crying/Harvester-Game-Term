from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from enum import Enum, auto
from faker import Faker
from item import listFoods
import uuid
import random
from item import Food, listFoods, ItemStack
from InquirerPy import inquirer
import subprocess
import sys
from utility import clear_screen

fake_name = Faker("en_US")


class WorldObject(ABC):
    def __init__(self, name, prefix):
        self.name = name
        self.__bornDate = date.today()
        self.isAlive = True
        self.idWO = f"{prefix}-{str(uuid.uuid4())[:8]}"

    def updateDay(self):
        pass

    def updateAlive(self):
        self.isAlive = False

    @abstractmethod
    def __str__(self):
        return f"""
                {self.name}
                {self.__bornDate}
                {self.isAlive}
                {self.idWO}
        """

    @property
    def age_in_days(self):
        return relativedelta(self.__bornDate, date.today())


class Animal(WorldObject, ABC):
    __sickProb = 4
    _next_y = 2  # class attribute, shared antar semua instance

    def __init__(self, name, gender, prefix):
        super().__init__(name, prefix)
        self.status = {
            "Hungry Status": AnimalStatus.NOTHUNGRY.name,
            "Sick Status": {
                "Condition": AnimalStatus.HEALTHY.name,
                "Disease": AnimalDisease.NONE.name,
            },
            "Harvest Status": AnimalStatus.NOTREADY.name,
            "Love Status": {"Condition": False, "Cooldown": 0},
            "Health": 100,  # max health 100
            "Relationship": 0,  # max Relationship 100
            "Stress": 0,  # max stress 10
        }
        self.dateLastMeal = date.today()
        self.gender = gender
        if gender == "Female":
            self.pregnant = False
        else:
            self.pregnant = "N\\A"

    def __str__(self):
        pregnant_info = (
            f"Pregnant: {self.pregnant}\n" if self.gender == "Female" else ""
        )

        return (
            f"Name: {self.name}\n"
            f"Is Alive: {self.isAlive}\n"
            f"Id: {self.idWO}\n"
            f"Health: {self.health}\n"
            f"Date Last Meal: {self.dateLastMeal}\n"
            f"Hungry: {self.status['Hungry Status']}\n"
            f"Harvest: {self.status['Harvest Status']}\n"
            f"Sick: {self.status['Sick Status']}\n"
            f"Stress: {self.status['Stress']}\n"
            f"Relationship: {self.status['Relationship']}\n"
            f"Love: {self.status['Love Status']['Condition']}\n"
            f"Pregnant: {self.pregnant}".strip()
        )

    @property
    def love(self):
        return self.status["Love Status"]["Condition"]

    @love.setter
    def love(self):
        if (
            self.age_in_days.days >= 365
            and self.status["Sick Status"]["Condition"] == AnimalStatus.HEALTHY.name
            and self.status["Hungry Status"] == AnimalStatus.NOTHUNGRY.name
            and self.status["Stress"] <= 5
        ):
            self.status["Love Status"]["Condition"] = True
        else:
            pass

    @property
    def health(self):
        return self.status["Health"]

    @health.setter
    def health(self):
        if self.status[
            "Hungry Status"
        ] == AnimalStatus.HUNGRY.name and self.dateLastMeal == (
            date.today()
        ) - timedelta(
            days=2
        ):
            self.health -= 2
            if self.health <= 0:
                self.isAlive = False
        else:
            self.health += 2

    @property
    def stress(self):
        return self.stress

    @stress.setter
    def stress(self):
        self.stress += 1

    @property
    def sick(self):
        return self.status["Sick Status"]

    @sick.setter
    def get_sick(self):
        if (
            self.status["Hungry Status"] == AnimalStatus.HUNGRY.name
        ):  # Probability animal get sick increase if the animal hungry
            self.__sickProb += 10
        else:
            self.__sickProb = 10
        if random.random() < self.__sickProb:
            self.status["Sick Status"]["Condition"] = AnimalStatus.SICK.name
            self.status["Sick Status"]["Disease"] = random.choice(list(AnimalDisease))

    @abstractmethod
    def check_accepted_consumption(self, consumption) -> bool:
        pass

    def cure_sick(self, consumption):
        if self.status["Sick Status"]["Condition"] == AnimalStatus.SICK.name:
            if (
                self.check_accepted_consumption(consumption)
                and f"{self.status['Sick Status']['Disease'].lower()}"
                in consumption.lower()
            ):
                self.status["Sick Status"]["Condition"] = AnimalStatus.HEALTHY.name
                self.status["Sick Status"]["Disease"] = None
        else:
            pass

    def eating(self, consumption):
        if self.status["Hungry Status"] == AnimalStatus.HUNGRY.name:
            if self.check_accepted_consumption(consumption):
                self.status["Hungry Status"] = AnimalStatus.NOTHUNGRY.name
                self.dateLastMeal = date.today()
            else:
                print(f"Sorry this meal not for your animal")
        else:
            pass

    def incress_stress(self):
        if (
            self.status["Harvest Status"] == AnimalStatus.READY.name
            or self.status["Hungry Status"] == AnimalStatus.HUNGRY.name
            or self.status["Sick Status"]["Condition"] == AnimalStatus.SICK.name
        ):
            self.stres += 1

    def get_info_image(self, path, info, img_cols=20, img_rows=10, x=0, y=0):
        subprocess.run(
            [
                "kitty",
                "+kitten",
                "icat",
                "--place",
                f"{img_cols}x{img_rows}@{x}x{y}",
                "--scale-up",
                path,
            ]
        )
        info_lines = info.split("\n")
        text_x = x + img_cols + 2
        for i, line in enumerate(info_lines):
            row = y + i
            print(f"\033[{row+1};{text_x+1}H{line}", end="")
        print(f"\033[{y+img_rows+1};1H", end="", flush=True)
        print("─" * 60)
        print()


class Cow(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, "COW")
        self.accepted_consumption = {
            "grass": {"type": "food"},
            "cow pellets": {"type": "food"},
            "dry grass": {"type": "food"},
            "cow flu medicine": {"type": "medicine"},
            "cow fever medicine": {"type": "medicine"},
            "cow virus medicine": {"type": "medicine"},
        }

    def check_accepted_consumption(self, consumption) -> bool:
        return consumption in self.accepted_consumption.keys()

    def get_info(self):
        img_rows = 12
        if self.isAlive:
            self.get_info_image(
                "assets/cow.png",
                super().__str__(),
                img_cols=20,
                img_rows=img_rows,
                x=0,
                y=Animal._next_y,
            )
        else:
            self.get_info_image(
                "assets/dead_cow.png",
                f"YOUR COW HAS BEEN DEAD",
                img_cols=20,
                img_rows=img_rows,
                x=0,
                y=Animal._next_y,
            )
        Animal._next_y += img_rows + 1


class Chicken(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender, "CHICKEN")
        self.accepted_consumption = {
            "grass": {"type": "food"},
            "chicken  pelltets": {"type": "food"},
            "chicken flu medicine": {"type": "medicine"},
            "chicken fever medicine": {"type": "medicine"},
            "chicken virus medicine": {"type": "medicine"},
        }

    def check_accepted_consumption(self, consumption) -> bool:
        return consumption in self.accepted_consumption.keys()

    def get_info(self):
        img_rows = 12
        if self.isAlive:
            self.get_info_image(
                "assets/chicken.png",
                super().__str__(),
                img_cols=20,
                img_rows=img_rows,
                x=0,
                y=Animal._next_y,
            )
        else:
            self.get_info_image(
                "assets/dead_chicken.png",
                "YOUR CHICKEN HAS BEEN DEAD",
                img_cols=20,
                img_rows=img_rows,
                x=0,
                y=Animal._next_y,
            )
        Animal._next_y += img_rows + 2


def show_animal(list_animal: list):
    i = 0
    while i < len(list_animal):
        list_animal[i].get_info()
        confirm = None
        if (i + 1) % 3 == 0 or i + 1 == len(list_animal):
            if i + 1 <= 3:
                confirm = inquirer.select(
                    message="Continue?",
                    choices=["Next", "Quit"],
                ).execute()
            elif i + 1 > 3:
                confirm = inquirer.select(
                    message="Continue?",
                    choices=["Prev", "Next", "Quit"],
                ).execute()
            if confirm == "Quit":
                return
            elif confirm == "Next":
                clear_screen()
                Animal._next_y = 2
                i += 1
                continue
            else:
                clear_screen()
                Animal._next_y = 2
                i -= 3
                continue
        i += 1
