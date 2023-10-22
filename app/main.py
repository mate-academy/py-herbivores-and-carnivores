from __future__ import annotations
from typing import Type


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def remove_dead_animal(cls, animal: Type[Herbivore]) -> None:
        cls.alive.remove(animal)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: Type[Herbivore]) -> None:
        if (isinstance(target, Herbivore)) and (not target.hidden):
            target.health -= 50
            if target.health <= 0:
                Animal.remove_dead_animal(target)
