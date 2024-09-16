class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)

    def __repr__(self):
        return f'{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}'


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if not animal.health:
                Animal.alive.remove(animal)
