class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
