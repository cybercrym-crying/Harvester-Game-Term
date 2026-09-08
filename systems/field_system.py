from entities.corp import Corp
from entities.item import ItemStack, Item, WateringCane


class Soil:
    def __init__(self):
        self.corp = None
        self.is_fertelized = False
        self.is_plowed = False
        self.is_watered = False


class FieldSystem:
    def __init__(self, rows=3, cols=3):
        self.field_size = [[Soil() for _ in range(cols)] for _ in range(rows)]

    def watering_field(self, row, cols, watering_cane: WateringCane):
        if watering_cane.use_water:
            self.field_size[row][cols].is_watered = True
        else:
            print("Sorry not enough water in your cane")
