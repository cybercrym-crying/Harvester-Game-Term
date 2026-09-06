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


class RarityType(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGEND = 5


RARITY_DROP_CHANCE = {
    RarityType.COMMON: 0.5,
    RarityType.UNCOMMON: 0.3,
    RarityType.RARE: 0.1,
    RarityType.EPIC: 0.08,
    RarityType.LEGEND: 0.02,
}
RARITY_PRICE_MULTIPLIER = {
    RarityType.COMMON: 1,
    RarityType.UNCOMMON: 2,
    RarityType.RARE: 5,
    RarityType.EPIC: 15,
    RarityType.LEGEND: 50,
}

BASE_PRICE_ITEM = {
    ItemType.MATERIAL: 2,
    ItemType.TOOLS: 3,
    ItemType.FOOD: 1,
    ItemType.SEED: 2,
}


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
        return date.today() - self.born_date

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
print(listFoods[0])
listMaterial = ["Diamond", "", 10, RarityType.EPIC, MaterialType.IRON]
