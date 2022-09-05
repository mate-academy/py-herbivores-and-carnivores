class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}," \
                     f" Health: {self.health}," \
                     f" Hidden: {self.hidden}" + "}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            if self.hidden is True:
                self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
