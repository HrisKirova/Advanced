from project import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care = Tiger.MONEY_FOR_CARE)
