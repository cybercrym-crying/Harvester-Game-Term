from world_object import WorldObject
from abc import ABC, abstractmethod
from core.enums import CorpType


class Corp(WorldObject):
    is_watered = False
    is_fertilized = False
    is_harvested = False
    days_lived = 0

    def __init__(self, name, days_to_grow, corp_type: CorpType):
        super().__init__(name, "CORP")
        self.name = name

        self.days_to_grow = days_to_grow
        self.corp_type = corp_type

    def __str__(self):
        return f"""
                    {self.name}
                    {self.__bornDate}
                    {self.is_alive}
                    {self.idWO}
                {self.is_watered}
                {self.is_fertilized}
                {self.days_lived}
                {self.corp_type.name}
            """

    def watering(self):
        self.is_watered = True

    def fertilizing(self):
        self.is_fertilized = True

    def ready_to_harvest(self):
        if self.days_lived == self.days_to_grow and self.is_alive == True:
            self.is_watered = True


list_corp = {"Tomato": Corp("Tomato", 3, CorpType.VEGETABLE)}
