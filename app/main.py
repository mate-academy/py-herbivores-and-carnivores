from __future__ import annotations
from typing import List, Any


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _check_health(self) -> None:
        """Remove from alive list if health reaches 0"""
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if (
            not isinstance(other, Herbivore)
            or other.hidden
            or other.health <= 0
        ):
            return
        other.health -= 50
        other._check_health()


def __str_alive__(cls: Any) -> str:
    return f"[{", ".join(repr(animal) for animal in cls.alive)}]"
