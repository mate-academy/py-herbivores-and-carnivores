from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def hide(self):
        self.hidden = not self.hidden

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', health={self.health}, hidden={self.hidden})"


class Herbivore(Animal):
    pass


class Carnivore(Animal):
    def bite(self, other: Animal):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
