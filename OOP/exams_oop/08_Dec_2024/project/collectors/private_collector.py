from project import BaseCollector


class PrivateCollector(BaseCollector):

    AVAILABLE_MONEY = 25000.0
    AVAILABLE_SPACE = 3000
    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)

    INCREASED_VALUE = 5000

    def increase_money(self):
        self.available_money += self.INCREASED_VALUE
