from project import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'Male')

    @staticmethod
    def make_sound():
        return "Hiss"
