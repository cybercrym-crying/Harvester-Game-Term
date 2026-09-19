from entities.world_object import WorldObject
from abc import ABC, abstractmethod
from datetime import date, timedelta
from core.enums import AnimalStatus, TypeDisease
from InquirerPy import inquirer
from utils.utility import clear_screen, check_term_size
import random
import subprocess


class Animal(WorldObject, ABC):
    __sickProb = 4  # base persen chance kena sakit
    _next_y = 2  # class attribute, shared antar semua instance untuk posisi gambar
    total_animal = 0  # jumlah total hewan yang hidup

    def __init__(self, name, gender, prefix):
        super().__init__(name, prefix)
        Animal.total_animal += 1
        self.__health = 100
        self.__stress = 0
        self.__relationship = 0
        self.__hungry_status = AnimalStatus.NOTHUNGRY.name
        self.__sick_condition = AnimalStatus.HEALTHY.name
        self.__sick_disease = TypeDisease.NONE.name
        self.__harvest_status = AnimalStatus.NOTREADY.name
        self.__love = False
        self.dateLastMeal = date.today()
        self.gender = gender
        if gender == "Female":
            self.pregnant = False
        else:
            self.pregnant = "N\\A"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Is Alive: {self.is_alive}\n"
            f"Id: {self.idWO}\n"
            f"Health: {self.__health}\n"
            f"Date Last Meal: {self.dateLastMeal}\n"
            f"Hungry: {self.__hungry_status}\n"
            f"Harvest: {self.__harvest_status}\n"
            f"Sick: {self.__sick_condition} ({self.__sick_disease})\n"
            f"Stress: {self.__stress}\n"
            f"Relationship: {self.__relationship}\n"
            f"Love: {self.__love}\n"
            f"Pregnant: {self.pregnant}".strip()
        )

    @classmethod
    def from_dict(cls, data: dict):
        animal = cls(data["name"], data["gender"])  # type: ignore[call-arg]
        animal.health = data.get("health", 100)
        animal.stress = data.get("stress", 0)
        animal.love = data.get("love", False)
        return animal

    @property
    def love(self):
        return self.__love

    @love.setter
    def love(self, value):
        # cuma bisa jadi True kalau syaratnya lengkap, selain itu tetap False
        if (
            self.age_in_days.days >= 365
            and self.__sick_condition == AnimalStatus.HEALTHY.name
            and self.__hungry_status == AnimalStatus.NOTHUNGRY.name
            and self.__stress <= 5
        ):
            self.__love = value
        else:
            self.__love = False

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if not isinstance(value, (int, float)):
            print("Health harus berupa angka!")
            return
        self.__health = max(0, min(100, value))
        if self.__health <= 0:
            self.is_alive = False
            Animal.total_animal -= 1

    @property
    def stress(self):
        return self.__stress

    @stress.setter
    def stress(self, value):
        if value < 0:
            print("Stress tidak boleh negatif!")
            return
        self.__stress = min(10, value)

    @property
    def sick(self):
        return {"Condition": self.__sick_condition, "TypeDisease": self.__sick_disease}

    @sick.setter
    def sick(self, value):
        if value not in (AnimalStatus.HEALTHY.name, AnimalStatus.SICK.name):
            print("Status sick tidak valid!")
            return
        self.__sick_condition = value

    @classmethod
    def get_total_animal(cls):
        return cls.total_animal

    @abstractmethod
    def check_accepted_consumption(self, consumption) -> bool:
        pass

    @staticmethod
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

    def update_health_by_hunger(self):
        if self.__hungry_status == AnimalStatus.HUNGRY.name and self.dateLastMeal == (
            date.today() - timedelta(days=2)
        ):
            self.health -= 2
        else:
            self.health += 2

    def get_sick(self):
        # Probability animal get sick increase if the animal hungry
        if self.__hungry_status == AnimalStatus.HUNGRY.name:
            chance = Animal.__sickProb + 10
        else:
            chance = Animal.__sickProb
        if random.random() * 100 < chance:
            self.sick = AnimalStatus.SICK.name
            self.__sick_disease = random.choice(list(TypeDisease)).name

    def cure_sick(self, consumption):
        if self.__sick_condition == AnimalStatus.SICK.name:
            if (
                self.check_accepted_consumption(consumption)
                and self.__sick_disease.lower() in consumption.lower()
            ):
                self.sick = AnimalStatus.HEALTHY.name
                self.__sick_disease = TypeDisease.NONE.name

    def eating(self, consumption):
        if self.__hungry_status == AnimalStatus.HUNGRY.name:
            if self.check_accepted_consumption(consumption):
                self.__hungry_status = AnimalStatus.NOTHUNGRY.name
                self.dateLastMeal = date.today()
            else:
                print(f"Sorry this meal not for your animal")

    def incress_stress(self):
        if (
            self.__harvest_status == AnimalStatus.READY.name
            or self.__hungry_status == AnimalStatus.HUNGRY.name
            or self.__sick_condition == AnimalStatus.SICK.name
        ):
            self.stress += 1

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
        if self.is_alive:
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
        if self.is_alive:
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
