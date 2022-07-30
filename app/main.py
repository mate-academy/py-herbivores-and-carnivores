class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        name = self.name
        health = self.health
        hidden = self.hidden
        return f'{{Name: {name}, Health: {health}, Hidden: {hidden}}}'


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal):
        if isinstance(animal, Carnivore):
            print("Carnivore can't bite carnivore")
        elif animal.hidden:
            print("lion cannot bite hidden rabbit")
        else:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
