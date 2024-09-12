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
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore):
        if not isinstance(other, Carnivore) and not other.hidden:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
