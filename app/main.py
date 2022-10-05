class Animal:
    alive = []

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Carnivore(Animal):
    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health == 0:
                Animal.alive.remove(animal)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
