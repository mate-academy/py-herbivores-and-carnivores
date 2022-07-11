class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        a = f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
        return f'{{{a}}}'


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
            return self.hidden
        self.hidden = False
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
