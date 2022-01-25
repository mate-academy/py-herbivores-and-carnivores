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
    def bite(animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
        if animal.health == 0:
            animal.alive.remove(animal)
