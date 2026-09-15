from entities.consumable_item import Food, Medicine
from entities.item import Tools, Material
from entities.character import Player
from entities.animal_wo import Animal
from entities.corp_wo import Corp
from entities.consumable_item import Consumable
from core.enums import (
    FoodType,
    MaterialType,
    RarityType,
    TypeDisease,
    CorpType,
    Effect,
)

list_material = {
    # --- Metal ---
    "Copper": Material("Copper", MaterialType.METAL, RarityType.COMMON),
    "Iron": Material("Iron", MaterialType.METAL, RarityType.COMMON),
    "Steel": Material("Steel", MaterialType.METAL, RarityType.UNCOMMON),
    "Silver": Material("Silver", MaterialType.METAL, RarityType.RARE),
    "Gold": Material("Gold", MaterialType.METAL, RarityType.RARE),
    "Mithril": Material("Mithril", MaterialType.METAL, RarityType.EPIC),
    "Adamantite": Material("Adamantite", MaterialType.METAL, RarityType.LEGEND),
    # --- Kayu ---
    "Oak Wood": Material("Oak Wood", MaterialType.WOOD, RarityType.COMMON),
    "Pine Wood": Material("Pine Wood", MaterialType.WOOD, RarityType.COMMON),
    "Mahogany": Material("Mahogany", MaterialType.WOOD, RarityType.UNCOMMON),
    "Ebony Wood": Material("Ebony Wood", MaterialType.WOOD, RarityType.RARE),
    # --- Batu / Mineral ---
    "Stone": Material("Stone", MaterialType.STONE, RarityType.COMMON),
    "Granite": Material("Granite", MaterialType.STONE, RarityType.COMMON),
    "Obsidian": Material("Obsidian", MaterialType.STONE, RarityType.UNCOMMON),
    "Marble": Material("Marble", MaterialType.STONE, RarityType.RARE),
    # --- Permata ---
    "Quartz": Material("Quartz", MaterialType.GEM, RarityType.COMMON),
    "Ruby": Material("Ruby", MaterialType.GEM, RarityType.RARE),
    "Sapphire": Material("Sapphire", MaterialType.GEM, RarityType.RARE),
    "Diamond": Material("Diamond", MaterialType.GEM, RarityType.EPIC),
    # --- Bahan organik / lainnya ---
    "Leather": Material("Leather", MaterialType.ORGANIC, RarityType.COMMON),
    "Cloth": Material("Cloth", MaterialType.ORGANIC, RarityType.COMMON),
    "Silk": Material("Silk", MaterialType.ORGANIC, RarityType.UNCOMMON),
    "Dragon Scale": Material("Dragon Scale", MaterialType.ORGANIC, RarityType.LEGEND),
}
list_tool = {
    # --- Shovel ---
    "Iron Shovel": Tools(
        "Iron Shovel", [list_material["Iron"], list_material["Mahogany"]]
    ),
    "Copper Shovel": Tools(
        "Copper Shovel", [list_material["Copper"], list_material["Oak Wood"]]
    ),
    "Steel Shovel": Tools(
        "Steel Shovel", [list_material["Steel"], list_material["Mahogany"]]
    ),
    # --- Pickaxe ---
    "Iron Pickaxe": Tools(
        "Iron Pickaxe", [list_material["Iron"], list_material["Oak Wood"]]
    ),
    "Steel Pickaxe": Tools(
        "Steel Pickaxe", [list_material["Steel"], list_material["Ebony Wood"]]
    ),
    "Mithril Pickaxe": Tools(
        "Mithril Pickaxe", [list_material["Mithril"], list_material["Ebony Wood"]]
    ),
    # --- Axe ---
    "Iron Axe": Tools("Iron Axe", [list_material["Iron"], list_material["Pine Wood"]]),
    "Steel Axe": Tools(
        "Steel Axe", [list_material["Steel"], list_material["Mahogany"]]
    ),
    # --- Hoe ---
    "Iron Hoe": Tools("Iron Hoe", [list_material["Iron"], list_material["Pine Wood"]]),
    "Steel Hoe": Tools(
        "Steel Hoe", [list_material["Steel"], list_material["Oak Wood"]]
    ),
    # --- Sickle (buat motong rumput/pakan ternak) ---
    "Iron Sickle": Tools(
        "Iron Sickle", [list_material["Iron"], list_material["Oak Wood"]]
    ),
    "Copper Sickle": Tools(
        "Copper Sickle", [list_material["Copper"], list_material["Pine Wood"]]
    ),
    "Steel Sickle": Tools(
        "Steel Sickle", [list_material["Steel"], list_material["Mahogany"]]
    ),
    "Milking Bucket": Tools(
        "Milking Bucket", [list_material["Iron"], list_material["Leather"]]
    ),
    "Feeding Trough": Tools(
        "Feeding Trough", [list_material["Oak Wood"], list_material["Stone"]]
    ),
    "Shears": Tools("Shears", [list_material["Steel"], list_material["Leather"]]),
    "Hay Fork": Tools("Hay Fork", [list_material["Iron"], list_material["Pine Wood"]]),
}

list_corp = {
    "Tomato": Corp("Tomato", 3, CorpType.VEGETABLE),
    "Corn": Corp("Corn", 4, CorpType.VEGETABLE),
    "Potato": Corp("Potato", 4, CorpType.VEGETABLE),
    "Carrot": Corp("Carrot", 3, CorpType.VEGETABLE),
    "Ginger": Corp("Ginger", 5, CorpType.HERB),
    "Turmeric": Corp("Turmeric", 5, CorpType.HERB),
    "Lemongrass": Corp("Lemongrass", 4, CorpType.HERB),
    "Galangal": Corp("Galangal", 5, CorpType.HERB),
    "Wheat": Corp("Wheat", 4, CorpType.GRAIN),
    "Rice": Corp("Rice", 5, CorpType.GRAIN),
}


list_herb = {
    "Ginger": Food(
        "Ginger",
        FoodType.HERB,
        [Player],
        [Effect.HEAL, Effect.STAMINA],
        RarityType.UNCOMMON,
    ),
    "Turmeric": Food(
        "Turmeric", FoodType.HERB, [Player, Animal], [Effect.HEAL], RarityType.COMMON
    ),
    "Aromatic Ginger": Food(
        "Aromatic Ginger", FoodType.HERB, [Player], [Effect.HEAL], RarityType.UNCOMMON
    ),
    "Lemongrass": Food(
        "Lemongrass", FoodType.HERB, [Player], [Effect.STAMINA], RarityType.COMMON
    ),
    "Galangal": Food(
        "Galangal", FoodType.HERB, [Player], [Effect.STAMINA], RarityType.COMMON
    ),
    "Pandan": Food(
        "Pandan", FoodType.HERB, [Animal], [Effect.STAMINA], RarityType.UNCOMMON
    ),
    "Cinnamon": Food(
        "Cinnamon", FoodType.HERB, [Player], [Effect.STAMINA], RarityType.RARE
    ),
    "Ginseng": Food(
        "Ginseng",
        FoodType.HERB,
        [Player],
        [Effect.HEAL, Effect.STAMINA],
        RarityType.LEGEND,
    ),
    "Basil": Food("Basil", FoodType.HERB, [Player], [Effect.HEAL], RarityType.COMMON),
    "Mint": Food("Mint", FoodType.HERB, [Player], [Effect.HEAL], RarityType.COMMON),
}

list_food = {
    "Rice": Food(
        "Rice", FoodType.GRAIN, [Player, Animal], [Effect.HEAL], RarityType.UNCOMMON
    ),
    "Wheat": Food(
        "Wheat", FoodType.GRAIN, [Player, Animal], [Effect.HEAL], RarityType.COMMON
    ),
    "Garlic": Food(
        "Garlic", FoodType.SPICE, [Player], [Effect.HEAL], RarityType.COMMON
    ),
    "Red Onion": Food(
        "Red Onion", FoodType.SPICE, [Player], [Effect.STAMINA], RarityType.COMMON
    ),
    "Chili": Food("Chili", FoodType.SPICE, [Player], [Effect.HEAL], RarityType.COMMON),
    "Chicken": Food(
        "Chicken",
        FoodType.MEAT,
        [Player],
        [Effect.HEAL, Effect.STAMINA],
        RarityType.UNCOMMON,
    ),
    "Beef": Food("Beef", FoodType.MEAT, [Player], [Effect.STAMINA], RarityType.RARE),
    "Mutton": Food(
        "Mutton", FoodType.MEAT, [Player], [Effect.STAMINA], RarityType.RARE
    ),
    "Egg": Food("Egg", FoodType.MEAT, [Player], [Effect.HEAL], RarityType.COMMON),
    "Milk": Food(
        "Milk", FoodType.DAIRY, [Player, Animal], [Effect.STAMINA], RarityType.COMMON
    ),
    "Cheese": Food(
        "Cheese", FoodType.DAIRY, [Player], [Effect.HEAL], RarityType.UNCOMMON
    ),
    "Tomato": Food(
        "Tomato", FoodType.VEGETABLE, [Player], [Effect.HEAL], RarityType.COMMON
    ),
    "Potato": Food(
        "Potato", FoodType.VEGETABLE, [Player], [Effect.STAMINA], RarityType.COMMON
    ),
    "Carrot": Food(
        "Carrot",
        FoodType.VEGETABLE,
        [Player, Animal],
        [Effect.HEAL],
        RarityType.COMMON,
    ),
    "Golden Apple": Food(
        "Golden Apple",
        FoodType.FRUIT,
        [Player],
        [Effect.HEAL, Effect.STAMINA],
        RarityType.LEGEND,
    ),
    "Apple": Food(
        "Apple", FoodType.FRUIT, [Player, Animal], [Effect.HEAL], RarityType.COMMON
    ),
}
list_meal = {
    "Fried Rice": Food(
        "Fried Rice",
        FoodType.MEAL,
        [Player],
        recipe=[list_food["Rice"], list_food["Red Onion"], list_food["Garlic"]],
    ),
    "Chicken Soup": Food(
        "Chicken Soup",
        FoodType.MEAL,
        [Player],
        recipe=[list_food["Chicken"], list_herb["Lemongrass"], list_herb["Galangal"]],
    ),
    "Beef Stew": Food(
        "Beef Stew",
        FoodType.MEAL,
        [Player],
        recipe=[list_food["Beef"], list_food["Potato"], list_food["Carrot"]],
    ),
    "Ginger Tea": Food(
        "Ginger Tea",
        FoodType.MEAL,
        [Player],
        recipe=[list_herb["Ginger"], list_herb["Lemongrass"]],
    ),
}
