from typing import List, Type

from project import Bird
from project import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

class Hen(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable, Meat, Fruit, Seed]

    @property
    def weight_coefficient(self) -> float:
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
