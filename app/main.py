class Animal:
    alive = []

    def __init__(self, name, hidden=False, health=100):
        self.health = health
        self.hidden = hidden
        self.name = name
        if self.health > 0:
            self.alive.append(self)

    def __bool__(self):
        return self.health > 0

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def die(self):
        if self in self.alive and self:
            self.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other.die()
