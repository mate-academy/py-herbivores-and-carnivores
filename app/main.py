# write your code here
class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        # cannot bite non-herbivores
        if not isinstance(animal, Herbivore):
            return

        # cannot bite hidden herbivores
        if animal.hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()