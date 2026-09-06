from datetime import date, timedelta


class TimeSystem:
    def __init__(self):
        self.__curr_data = date.today()

    def next_day(self, amount_days=1):
        self.__curr_date += timedelta(days=amount_days)

    def get_date(self):
        return self.__curr_date


clock = TimeSystem()
