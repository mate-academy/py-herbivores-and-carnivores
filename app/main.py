class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden=False):
        Animal.alive.append(self)
        self.name = name
        self.health = health
        self.hidden = hidden

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if other.hidden is False and type(other) != type(self):
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
