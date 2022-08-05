class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = not False
        elif self.hidden is True:
            self.hidden = not True
        return self


class Carnivore(Animal):

    @classmethod
    def bite(cls, self):
        if isinstance(self, Herbivore) and self.hidden is False:
            self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)

        return self
