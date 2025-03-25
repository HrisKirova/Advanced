from typing import List

from project import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers = []



    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        searched_worker = next((w for w in self.workers if w.name == worker_name), None)
        if searched_worker is not None:
            self.workers.remove(searched_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum(worker.salary for worker in self.workers):
            self.__budget -= sum(worker.salary for worker in self.workers)
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= sum(animal.money_for_care for animal in self.animals):
            self.__budget -= sum(animal.money_for_care for animal in self.animals)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']


        result = [f"You have {total_animals_count} animals"]

        if lions:
            result.append(f"----- {len(lions)} Lions:")
            result.extend(str(lion) for lion in lions)  # Using __repr__()

        if tigers:
            result.append(f"----- {len(tigers)} Tigers:")
            result.extend(str(tiger) for tiger in tigers)  # Using __repr__()

        if cheetahs:
            result.append(f"----- {len(cheetahs)} Cheetahs:")
            result.extend(str(cheetah) for cheetah in cheetahs)  # Using __repr__()

        return "\n".join(result)

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [b for b in self.workers if b.__class__.__name__ == 'Keeper']
        caretakers = [b for b in self.workers if b.__class__.__name__ == 'Caretaker']
        vets = [b for b in self.workers if b.__class__.__name__ == 'Vet']

        result = [f"You have {total_workers_count} workers"]

        if keepers:
            result.append(f"----- {len(keepers)} Keepers:")
            result.extend(str(keeper) for keeper in keepers)  # Using __repr__()

        if caretakers:
            result.append(f"----- {len(caretakers)} Caretakers:")
            result.extend(str(caretaker) for caretaker in caretakers)  # Using __repr__()

        if vets:
            result.append(f"----- {len(vets)} Vets:")
            result.extend(str(vet) for vet in vets)  # Using __repr__()

        return "\n".join(result)



