class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, other):
        if not isinstance(other, Carnivore) and other.hidden is False:
            other.health -= 50
        if other.health <= 0:
            ind = self.__class__.alive.index(other)
            self.__class__.alive.pop(ind)
