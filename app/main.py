class Animal:
    alive = []

    def __init__(self, name=None, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        if self not in Animal.alive and self.health > 0:
            Animal.alive.append(self)
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
