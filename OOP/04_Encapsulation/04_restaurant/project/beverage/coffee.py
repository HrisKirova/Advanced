from project import HotBeverage


class Coffee(HotBeverage):

    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine: float) -> None:
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self) -> float:
        return self.__caffeine

