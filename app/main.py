class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return '{' + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + '}'


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, name):
        if name.hidden is False and isinstance(name, Herbivore):
            name.health -= 50
        if name.health <= 0:
            del Animal.alive[Animal.alive.index(name)]
