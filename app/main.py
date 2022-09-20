class Animal:
    alive = []

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.health = health
        self.hidden = hidden
        self.name = name
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore):
            if other.hidden is False:
                other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
