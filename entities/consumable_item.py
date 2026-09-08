from .item import Item
from .character import Player
from .animal_wo import Animal
from .corp_wo import Corp, list_corp
from core.enums import ItemType, RarityType, FoodType, TypeDisease
from abc import ABC, abstractmethod


class Consumable(Item):
    def __init__(self, name, rarity):
        super().__init__(name, ItemType.CONSUMABLE, rarity)


# jika tipe makanan menggunakan recipe berarti rarity di ambil dari recipe
# jika tipe makanan tidak menggunakan recipe berarti rarity di ambil dari masukan
class Food(Consumable):
    def __init__(self, name, food_type, rarity=None, recipe: list[Food] | None = None):
        self.food_type = food_type
        self.recipe = recipe or []
        if self.recipe:
            rarity = max((rcp.rarity for rcp in self.recipe), key=lambda r: r.value)
        super().__init__(name, rarity)


class Medicine(Consumable):
    def __init__(
        self,
        name,
        amount_health,
        type_disease: TypeDisease,
        target_class: type[Player | Animal],
        recipe: list[Food],
    ):
        self.type_disease = type_disease
        self.amount_health = amount_health
        self.target_class = target_class
        self.recipe = recipe
        rarity = max((rcp.rarity for rcp in self.recipe), key=lambda r: r.value)
        super().__init__(name, rarity)


class Fertilizer(Consumable):
    def __init__(self, name):
        super().__init__(name, RarityType.COMMON)


class Seed(Consumable):
    def __init__(self, name, rarity, corp_type: Corp):
        super().__init__(name, rarity)
        self.corp_type = corp_type


list_herb = {
    "Ginger": Food("Ginger", FoodType.HERB, RarityType.UNCOMMON),
    "Turmeric": Food("Turmeric", FoodType.HERB, RarityType.COMMON),
}
list_food = {
    "Rice": Food("Rice", FoodType.GRAIN, RarityType.UNCOMMON),
    "White Onion": Food("White Onion", FoodType.FRUIT, RarityType.COMMON),
}
list_player_medicine = {
    "flu": Medicine(
        "Flu Medicine",
        10,
        TypeDisease.FLU,
        Player,
        [list_herb["Ginger"], list_herb["Turmeric"]],
    )
}

list_meal = [
    Food(
        "Fried Rice",
        FoodType.MEAL,
        recipe=[list_food["Rice"], list_food["White Onion"]],
    )
]

list_seed = {"Tomato Seed": Seed("Tomato Seed", RarityType.COMMON, list_corp["Tomato"])}
