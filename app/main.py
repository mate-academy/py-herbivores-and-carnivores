from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:

        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def reduce_health(
        self, health: int
    ) -> None:

        self.health = max(0, self.health - health)

        if self.health == 0:
            Animal.alive.remove(self)

    def __repr__(
        self
    ) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(
        self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        animal: Animal
    ) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.reduce_health(50)
