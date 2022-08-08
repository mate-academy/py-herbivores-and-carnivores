class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if self.hidden is not True else False


class Carnivore(Animal):
    def bite(self, herbivore):
        for index, animal in enumerate(Animal.alive):
            if isinstance(animal, Carnivore) is False \
                    and herbivore.hidden is False:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    Animal.alive.pop(index)
