class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return f"\u007bName: {self.name}, Health: {self.health}," \
               f" Hidden: {self.hidden}\u007d"

    def hidden(self):
        return self.hidden


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if other.health == 0:
            other.alive.remove(other)
