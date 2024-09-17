class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
