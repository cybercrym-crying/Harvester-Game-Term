from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import date
from dateutil.relativedelta import relativedelta
from main import clock
from core.enums import (
    RarityType,
    ItemType,
    ItemCondition,
    MaterialType,
    Season,
    BASE_PRICE_ITEM,
    RARITY_PRICE_MULTIPLIER,
    RARITY_DROP_CHANCE,
)


class Item(ABC):
    def __init__(self, name, item_type, rarity, max_stack=33):
        self.name = name
        self.max_stack = max_stack
        self.rarity = rarity
        self._item_type = item_type
        self.__price = round(
            BASE_PRICE_ITEM[item_type] * RARITY_PRICE_MULTIPLIER[rarity]
        )
        self.__condition = ItemCondition.GOOD

    def __str__(self):
        return (
            f"Name      \t: {self.name}\n"
            f"Price     \t: {self.__price}\n"
            f"Condition\t: {self.__condition.name}\n"
            f"Type      \t: {self._item_type.name}\n"
        )

    def get_info(self):
        return {
            "name": self.name,
            "price": self.__price,
            "condition": self.__condition,
            "type": self._item_type,
        }


class ItemStack:
    def __init__(self, item: Item, quantity: int = 1):
        self.item = item
        self.__quantity = quantity

    def add_quantity(self, amount):
        if self.item._item_type == ItemType.TOOLS:
            self.__quantity += 1
            return amount - 1
        slot_left = self.item.max_stack - self.__quantity
        if slot_left <= 0:
            return amount
        added_amount = min(slot_left, amount)
        self.__quantity += added_amount
        return amount - added_amount

    def subtract_quantity(self, amount):
        if self.item._item_type != ItemType.TOOLS and self.__quantity - amount > 1:
            self.__quantity -= amount

    def get_info(self):
        data = self.item.get_info()
        data["quantity"] = self.__quantity
        return data

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, amount):
        self.__quantity = amount


class Tools(Item):
    def __init__(self, name, dura, materials: list[Material]):
        rarity = max((m.rarity for m in materials), key=lambda r: r.value)
        super().__init__(name, ItemType.TOOLS, rarity, 1)
        self.durability = dura
        self.materials = materials


class Food(Item):
    def __init__(self, name, calorie, rarity):
        super().__init__(name, ItemType.FOOD, rarity)
        self.born_date = date.today()
        self.calorie = calorie

    @property
    def age_in_days(self):
        return clock.get_date() - self.born_date

    def rotten(self):
        if self.age_in_days.days >= 5:
            self.condition = ItemCondition.ROTTEN.name


class Material(Item):
    def __init__(self, name, material_type: MaterialType, rarity: RarityType):
        super().__init__(
            name,
            ItemType.MATERIAL,
            rarity,
        )
        self.material_type = material_type


class Seed(Item):
    def __init__(
        self,
        name: str,
        growthPeriodInDays: int,
        season: Season,
        rarity: RarityType,
    ):
        super().__init__(name, ItemType.SEED, rarity)
        self.growthPeriod = growthPeriodInDays
        self.season = season


listFoods = [
    Food("G MILK 🥛", 40, RarityType.EPIC),
    Food("M MILK 🥛", 30, RarityType.UNCOMMON),
    Food("S MILK 🥛", 15, RarityType.COMMON),
]
listMaterial = ["Diamond", "", 10, RarityType.EPIC, MaterialType.IRON]
