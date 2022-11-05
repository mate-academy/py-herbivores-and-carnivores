class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f'{{Name: {self.name},' \
               f' Health: {self.health}, Hidden: {self.hidden}}}'


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden
        return self.hidden

    def alive(self):
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):

    @staticmethod
    def bite(other):

        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
