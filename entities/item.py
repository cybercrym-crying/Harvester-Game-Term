from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import date
from dateutil.relativedelta import relativedelta
from data.item_data import list_material
from core.enums import (
    RarityType,
    ItemType,
    ItemCondition,
    MaterialType,
    BASE_PRICE_ITEM,
    RARITY_MULTIPLIER,
    RARITY_DROP_CHANCE,
)
from systems.time_system import clock


class Item(ABC):
    def __init__(self, name, item_type, rarity, max_stack=33):
        self.name = name
        self.max_stack = max_stack
        self.rarity = rarity
        self._item_type = item_type
        self.__price = round(BASE_PRICE_ITEM[item_type] * RARITY_MULTIPLIER[rarity])
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
    def __init__(self, name, materials: list[Material]):
        rarity = max((m.rarity for m in materials), key=lambda r: r.value)
        super().__init__(name, ItemType.TOOLS, rarity, 1)
        self.durability = RARITY_MULTIPLIER[rarity] * 10
        self.materials = materials


class WateringCane(Tools):
    def __init__(self):
        super().__init__("Watering Cane", [list_material["Silver"]])
        self.max_water = 100
        self.curr_water = 100

    def fill_water(self):
        self.curr_water = 100

    def use_water(self, amount):
        if amount >= self.curr_water:
            return False
        else:
            self.curr_water = -amount
            return True


class Material(Item):
    def __init__(self, name, material_type: MaterialType, rarity: RarityType):
        super().__init__(
            name,
            ItemType.MATERIAL,
            rarity,
        )
        self.material_type = material_type
