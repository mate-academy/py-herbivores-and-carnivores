class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):

    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
