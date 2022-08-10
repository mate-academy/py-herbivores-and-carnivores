class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @classmethod
    def bite(cls, self):
        if isinstance(self, Herbivore) and self.hidden is False:
            self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)
