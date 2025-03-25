from project import BaseCollector


class Museum(BaseCollector):

    AVAILABLE_MONEY = 15000.0
    AVAILABLE_SPACE = 2000

    def __init__(self, name):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)

    INCREASED_VALUE = 1000
    def increase_money(self):
        self.available_money += self.INCREASED_VALUE


