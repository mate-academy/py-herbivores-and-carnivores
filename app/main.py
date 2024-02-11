class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden

        if self.health > 0:
            self.__class__.alive.append(self)

    def __repr__(self):
        return f"\x7BName: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}\x7D"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if other in Animal.alive and other.health <= 0:
            Animal.alive.remove(other)
