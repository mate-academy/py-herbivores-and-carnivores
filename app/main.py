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

    @staticmethod
    def __str__():
        return str([repr(animal) for animal in Animal.alive])


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        if not isinstance(herbivore, Herbivore):
            return  # Can't bite other carnivores
        if herbivore.hidden:
            return  # Can't bite hidden herbivores

        herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.die()
