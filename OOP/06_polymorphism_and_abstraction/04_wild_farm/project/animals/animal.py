from abc import ABC, abstractmethod
from typing import List, Type

from project import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    @abstractmethod
    def allowed_food(self) -> List[Type[Food]]:
        pass

    @property
    @abstractmethod
    def weight_coefficient(self) -> float:
        pass


    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    def feed(self, food):
        if type(food) not in self.allowed_food:
            # can work with food.__class__.__name__ too
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.weight_coefficient
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight) # we don't pass food_eaten because it has default value'
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"