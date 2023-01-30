from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Herbivore) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
                if animal.health <= 0:
                    Animal.alive.remove(animal)
