from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Animal:
    alive = []  # class attribute

    name: str
    health: int = 100
    hidden: bool = False

    # add instance to Class list(alive) after init
    def __post_init__(self) -> None:
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore) or herbivore.hidden:
            return
        if herbivore in Animal.alive:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
