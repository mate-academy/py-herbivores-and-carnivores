class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}, "\
            f"Health: {self.health}, Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore):
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
