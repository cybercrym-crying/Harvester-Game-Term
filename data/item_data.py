from entities.consumable_item import Food, Medicine, Seed
from entities.character import Player
from entities.animal_wo import Animal
from entities.corp_wo import Corp
from entities.consumable_item import Consumable
from core.enums import FoodType, MaterialType, RarityType, TypeDisease, CorpType

list_item = {"Fertelizer": Consumable("Fertelizer", RarityType.COMMON)}
list_corp = {
    "Tomato": Corp("Tomato", 3, CorpType.VEGETABLE),
    "Corn": Corp("Corn", 4, CorpType.VEGETABLE),
    "Ginger": Corp("Ginger", 5, CorpType.HERB),
    "Turmeric": Corp("Turmeric", 5, CorpType.HERB),
}

list_seed = {
    "Tomato Seed": Seed("Tomato seed", RarityType.COMMON, list_corp["Tomato"]),
    "Corn Seed": Seed("Corn seed", RarityType.UNCOMMON, list_corp["Corn"]),
    "Ginger Seed": Seed("Ginger seed", RarityType.UNCOMMON, list_corp["Ginger"]),
    "Turmeric Seed": Seed("Ginger seed", RarityType.UNCOMMON, list_corp["Turmeric"]),
}

list_herb = {
    "Ginger": Food("Ginger", FoodType.HERB, RarityType.UNCOMMON),
    "Turmeric": Food("Turmeric", FoodType.HERB, RarityType.COMMON),
    "Aromatic Ginger": ("Aromatic Ginger", FoodType.HERB, RarityType.UNCOMMON),
    "Lemongrass": Food("Lemongrass", FoodType.HERB, RarityType.COMMON),
    "Galangal": Food("Galangal", FoodType.HERB, RarityType.COMMON),
    "Pandan": Food("Pandan", FoodType.HERB, RarityType.UNCOMMON),
    "Cinnamon": Food("Cinnamon", FoodType.HERB, RarityType.RARE),
    "Ginseng": Food("Ginseng", FoodType.HERB, RarityType.LEGEND),
}
list_food = {
    "Rice": Food("Rice", FoodType.GRAIN, RarityType.UNCOMMON),
    "Garlic": Food("Garlic", FoodType.SPICE, RarityType.COMMON),
    "Red onion": Food("Red Onion", FoodType.SPICE, RarityType.COMMON),
    "Chicken": Food("Chicken", FoodType.MEAT, RarityType.UNCOMMON),
    "Beef": Food("Beef", FoodType.MEAT, RarityType.RARE),
    "Tomato": Food("Tomato", FoodType.VEGETABLE, RarityType.COMMON),
    "Golden apple": Food("Golden Apple", FoodType.FRUIT, RarityType.LEGEND),
}
list_player_medicine = {
    "Flu medicine": Medicine(
        "Flu medicine",
        10,
        TypeDisease.FLU,
        Player,
        [list_herb["Ginger"], list_herb["Turmeric"]],
    ),
    "Fever medicine": Medicine(
        "Fever medicine",
        4,
        TypeDisease.FEVER,
        Player,
        [list_herb["Ginger"], list_herb["Garlic"]],
    ),
    "Virus medicine": Medicine(
        "Virus medicine",
        20,
        TypeDisease.VIRUS,
        Player,
        [list_herb["Ginger"], list_herb["Cinnamon"], list_herb["Pandan"]],
    ),
}

list_meal = [
    Food(
        "Fried Rice",
        FoodType.MEAL,
        recipe=[list_food["Rice"], list_food["Red Onion"], list_food["Garlic"]],
    )
]
