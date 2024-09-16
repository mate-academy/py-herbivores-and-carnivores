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

    def die(self):
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False
        return self


class Carnivore(Animal):

    def bite(self, other):
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                other.die()
