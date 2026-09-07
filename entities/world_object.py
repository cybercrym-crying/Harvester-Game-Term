from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from abc import ABC, abstractmethod
from enum import Enum, auto
from faker import Faker
import uuid
import random
from InquirerPy import inquirer
import subprocess
import sys
from utils.utility import clear_screen


class WorldObject(ABC):
    def __init__(self, name, prefix):
        self.name = name
        self.is_alive = True
        self.idWO = f"{prefix}-{str(uuid.uuid4())[:8]}"
        self.__bornDate = date.today()

    def update_alive(self):
        self.is_alive = False

    @abstractmethod
    def __str__(self):
        return f"""
                {self.name}
                {self.__bornDate}
                {self.is_alive}
                {self.idWO}
        """

    @property
    def age_in_days(self):
        return relativedelta(self.__bornDate, date.today())
