class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden=False):
        Animal.alive.append(self)
        self.name = name
        self.health = health
        self.hidden = hidden

    def __repr__(self):
        feature = '{Name: ' + self.name + ', Health: ' + str(self.health) + \
                  ', Hidden: ' + str(self.hidden) + '}'
        return feature


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if other.hidden is False and type(other) != type(self):
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
