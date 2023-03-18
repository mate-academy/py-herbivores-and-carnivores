class Animal:
    alive = []

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other_animal):
        if isinstance(other_animal, Herbivore)\
                and not other_animal.hidden:
            other_animal.health -= 50
        if other_animal.health <= 0:
            f"{other_animal.name} is dead"
            Animal.alive.remove(other_animal)
        if other_animal.hidden:
            f"{self.name} cannot bite hidden {other_animal.name}"
