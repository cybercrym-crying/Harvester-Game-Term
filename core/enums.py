from enum import Enum, auto


class AnimalStatus(Enum):
    HUNGRY = auto()
    NOTHUNGRY = auto()
    SICK = auto()
    HEALTHY = auto()
    READY = auto()
    NOTREADY = auto()


class TypeDisease(Enum):
    FEVER = auto()
    FLU = auto()
    VIRUS = auto()
    NONE = auto()


class ItemCondition(Enum):
    GOOD = auto()
    BROKEN = auto()
    ROTTEN = auto()


class ItemType(Enum):
    TOOLS = auto()
    CONSUMABLE = auto()
    MATERIAL = auto()
    SEED = auto()


class MaterialType(Enum):
    WOOD = auto()
    IRON = auto()
    HERB = auto()
    STONE = auto()


class CorpType(Enum):
    HERB = auto()
    FLOWER = auto()
    FRUIT = auto()
    VEGETABLE = auto()


class RarityType(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGEND = 5


class FoodType(Enum):
    FRUIT = auto()
    VEGETABLE = auto()
    MEAL = auto()
    GRAIN = auto()
    HERB = auto()
    SPICE = auto()
    MEAT = auto()


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
    ItemType.CONSUMABLE: 1,
    ItemType.SEED: 2,
}
