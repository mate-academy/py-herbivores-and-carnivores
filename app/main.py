from __future__ import annotations
from typing import Union


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

    def __repr__(self) -> str:
        name = "{Name: " + str(self.name)
        health = ", Health: " + str(self.health)
        hidden = ", Hidden: " + str(self.hidden) + "}"
        return name + health + hidden


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Union[Herbivore, Carnivore]) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
        for index, beast in enumerate(Animal.alive):
            if beast.health <= 0:
                del Animal.alive[index]
