
class Animal:
    alive = []

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50

            if animal.health <= 0:
                Animal.alive.remove(animal)
