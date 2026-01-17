class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
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

    @staticmethod
    def bite(other_animal):
        if isinstance(other_animal, Herbivore) \
                and other_animal.hidden is False:
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)
