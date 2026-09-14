from .item import Item
from .character import Player
from .animal_wo import Animal
from .corp_wo import Corp
from core.enums import (
    ItemType,
    RarityType,
    FoodType,
    TypeDisease,
    Effect,
    BASE_EFFECT,
    RARITY_MULTIPLIER,
)
from abc import ABC, abstractmethod
from copy import deepcopy
import math


class Consumable(Item):
    def __init__(self, name, rarity):
        super().__init__(name, ItemType.CONSUMABLE, rarity)


# jika tipe makanan menggunakan recipe berarti rarity di ambil dari recipe
# jika tipe makanan tidak menggunakan recipe berarti rarity di ambil dari masukan
class Food(Consumable):
    def __init__(
        self,
        name,
        food_type,
        effect: list[Effect] = [],
        rarity=RarityType.COMMON,
        recipe: list[Food] = [],
    ):
        self.effect = effect or []
        self.recipe = recipe or []
        self.food_type = food_type
        temp_effect = {}
        if not self.recipe:
            for e in self.effect:
                temp_effect[e] = math.ceil(BASE_EFFECT[e] * RARITY_MULTIPLIER[rarity])
            self.effect = deepcopy(temp_effect)
            temp_effect.clear()
        else:
            rarity = max((rcp.rarity for rcp in self.recipe), key=lambda r: r.value)
            for r in recipe:
                for e in r.effect:
                    temp_effect[e] = 0
            for k, v in temp_effect.items():
                temp_effect[k] = math.ceil(
                    BASE_EFFECT[k]
                    * RARITY_MULTIPLIER[rarity]
                    * (math.ceil(len(self.recipe) * 0.6))
                )
            self.effect = deepcopy(temp_effect)
            temp_effect.clear()

        super().__init__(name, rarity)

    def __str__(self):
        if isinstance(self.effect, dict):
            list_effect = ", ".join(f"{k.name} +{v}" for k, v in self.effect.items())
            list_recipe = (
                ", ".join(f"{r.name}" for r in self.recipe) if self.recipe else None
            )
            return (
                f"Name:  \t{self.name}\n"
                f"Type:  \t{self.food_type.name}\n"
                f"Rarity:\t{self.rarity.name}\n"
                f"Effect:\t{list_effect}\n"
                f"Recipe:\t{list_recipe}\n"
            )
        return ""


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
