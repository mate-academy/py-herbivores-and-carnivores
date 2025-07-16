from typing import List


class Animal:
    name: str
    health: int
    hidden: bool
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        if herbivore.hidden:
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            if herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
