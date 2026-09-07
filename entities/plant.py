from world_object import WorldObject
from abc import ABC, abstractmethod
from core.enums import CorpType


class Corp(WorldObject):
    def __init__(self, name, days_to_grow, corp_type: CorpType):
        super().__init__(name, "CORP")
        self.name = name
        self.is_watered = False
        self.is_fertilized = False
        self.is_harvested = False
        self.days_lived = 0
        self.days_to_grow = days_to_grow
        self.corp_type = corp_type

    def __str__(self):
        return f"""
                    {self.name}
                    {self.__bornDate}
                    {self.isAlive}
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
        if self.days_lived == self.days_to_grow and self.isAlive == True:
            self.is_watered = True


corp = Corp("Tomato", 3, CorpType.VEGETABLE)
