from __future__ import annotations
from typing import Union


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = None
    ) -> None:
        self.name = name
        self.health = health if health is not None else 100
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore (Animal):
    def bite(self, animal: Union[Carnivore, Herbivore]) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                self.alive.remove(animal)
