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

    def bite(self, animal):
        if isinstance(animal, Carnivore):
            print(f"Carnivore can't bite {animal.name}")
        elif animal.hidden:
            print(f"{self.name} cannot bite hidden {animal.name}")
        else:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
