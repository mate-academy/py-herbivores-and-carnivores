from __future__ import annotations
from typing import ClassVar


class Animal:
    alive: ClassVar[list["Animal"]] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    DAMAGE = 50

    def bite(
            self,
            animal: Animal,
    ) -> None:
        if animal not in Animal.alive:
            return
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return

        animal.health -= self.DAMAGE
        if animal.health <= 0:
            animal.die()
