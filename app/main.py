from __future__ import annotations
from typing import ClassVar, List


class Animal:
    alive: ClassVar[List["Animal"]] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def _die(self) -> None:
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
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return

        if target.hidden:
            return

        target.health -= 50

        if target.health <= 0:
            target.health = 0
            target._die()
