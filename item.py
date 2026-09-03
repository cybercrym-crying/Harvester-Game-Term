from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import date
from dateutil.relativedelta import relativedelta


class ItemCondition(Enum):
    GOOD = auto()
    BROKEN = auto()
    ROTTEN = auto()


class ItemType(Enum):
    TOOLS = auto()
    FOOD = auto()
    MATERIAL = auto()
    SEED = auto()


class MaterialType(Enum):
    WOOD = auto()
    IRON = auto()
    HERB = auto()
    STONE = auto()


class Season(Enum):
    SPRING = auto()
    SUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()


class Item(ABC):
    def __init__(
        self,
        name: str,
        description: str,
        price: int,
        item_type: ItemType,
        max_stack: int = 33,
    ):
        self.name = name
        self.description = description
        self.max_stack = max_stack
        self._item_type = item_type
        self.__price = price
        self.__condition = ItemCondition.GOOD.name

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
    def __init__(self, name: str, description: str, price: int, durability: int):
        super().__init__(name, description, price, ItemType.TOOLS, 1)
        self.durability = durability

    def useTools(self):
        self.durability -= 1
        if self.durability <= 0:
            self.condition = ItemCondition.BROKEN.name


class Food(Item):
    def __init__(self, name: str, description: str, price: int, calorie: int):
        super().__init__(name, description, price, ItemType.FOOD)
        self.bornDate = date.today()
        self.calorie = calorie

    @property
    def ageInDays(self):
        return date.today() - self.bornDate

    def rotten(self):
        if self.ageInDays.days >= 5:
            self.condition = ItemCondition.ROTTEN.name


class Material(Item):
    def __init__(self, name, description, price, rarity, material_type: MaterialType):
        super().__init__(name, description, price, ItemType.MATERIAL)
        self.rarity = rarity
        self.material_type = material_type
        self.is_process = False


class Seed(Item):
    def __init__(
        self,
        name: str,
        description: str,
        price: int,
        growthPeriodInDays: int,
        season: Season,
    ):
        super().__init__(name, description, price, ItemType.SEED)
        self.growthPeriod = growthPeriodInDays
        self.season = season


listTools = [Tools("Sycthe Stone", "...", 3, 30), Tools("Pickaxe Stone", "...", 4, 33)]
listFoods = [
    Food("G MILK 🥛", "...", 40, 50),
    Food("M MILK 🥛", "...", 30, 30),
    Food("S MILK 🥛", "...", 15, 15),
]
listMaterial = [
    Material("Iron Ore", "Just Iron...", 3, 2, MaterialType.IRON),
    Material("Wood", "..", 1, 1, MaterialType.WOOD),
]
