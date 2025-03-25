from project import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories: float) -> None:
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self) -> float:
        return self.__calories

