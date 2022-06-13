class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f'' \
               f'{{'f'Name: {self.name}, ' \
               f'Health: {self.health}, ' \
               f'Hidden: {self.hidden}}}'


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(other):
        if isinstance(other, Carnivore) or other.hidden is True:
            other.health = other.health
        else:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
