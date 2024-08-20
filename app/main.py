class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{" + (f"Name: {self.name}, "
                      f"Health: {self.health}, "
                      f"Hidden: {self.hidden}") + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: ("Herbivore", "Carnivore")) -> None:
        if (self.__class__ is Carnivore and
                other.__class__ is Herbivore and
                other.hidden is False):
            other.health -= 50
            if other.health <= 0:
                self.alive.pop(self.alive.index(other))
