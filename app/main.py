from typing import List


class Animal:

    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        if health <= 0:
            raise ValueError("Health is too low")
        self.name = name
        self.health = health
        Animal.alive.append(self)
        self.hidden = False

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other_herbivore: Herbivore) -> None:
        if (isinstance(other_herbivore, Herbivore)
                and other_herbivore.hidden is False):
            other_herbivore.health -= 50
            if other_herbivore.health <= 0:
                Animal.alive.remove(other_herbivore)
