class Animal:
    alive = []

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            self.alive.append(self)

    def __bool__(self):
        return self.health > 0

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def dead(self):
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
            other.dead()
