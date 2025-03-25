from project import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care = Cheetah.MONEY_FOR_CARE)
