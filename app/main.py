class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health = other.health - 50
        if other.health < 1:
            return Animal.alive.remove(other)
