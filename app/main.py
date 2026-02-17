from __future__ import annotations
from typing import Any


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(
        self,
        value: int
    ) -> None:
        self._health = value
        if self._health <= 0:
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
    def bite(
        self,
        target: Any
    ) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
