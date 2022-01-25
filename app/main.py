class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other):
        if isinstance(other, Herbivore) and other.hidden is not True:
            other.health -= 50
        if other.health <= 0:
            self.alive.remove(other)
