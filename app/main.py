class Animal:

    alive = []

    def __init__(self, name: str, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        a, b = "{", "}"
        animal = f"Name: {self.name}, Health: {self.health}" \
                 f", Hidden: {self.hidden}"
        correct = a + animal + b
        return correct


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @classmethod
    def bite(cls, animal):
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
