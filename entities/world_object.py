from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from enum import Enum, auto
from faker import Faker
from item import listFoods
import uuid
import random
from item import Food, listFoods, ItemStack
from InquirerPy import inquirer
import subprocess
import sys
from utils.utility import clear_screen


class WorldObject(ABC):
    def __init__(self, name, prefix):
        self.name = name
        self.__bornDate = date.today()
        self.isAlive = True
        self.idWO = f"{prefix}-{str(uuid.uuid4())[:8]}"

    def updateDay(self):
        pass

    def updateAlive(self):
        self.isAlive = False

    @abstractmethod
    def __str__(self):
        return f"""
                {self.name}
                {self.__bornDate}
                {self.isAlive}
                {self.idWO}
        """

    @property
    def age_in_days(self):
        return relativedelta(self.__bornDate, date.today())
