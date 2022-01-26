class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health:" \
               f" {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore):
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health == 0:
            Animal.alive.remove(herbivore)
