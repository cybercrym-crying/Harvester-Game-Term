from .item import Item
from .character import Player
from .animal_wo import Animal
from .corp_wo import Corp
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


class Seed(Consumable):
    def __init__(self, name, rarity, corp_type: Corp):
        super().__init__(name, rarity)
        self.corp_type = corp_type
