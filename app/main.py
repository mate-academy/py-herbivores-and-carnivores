from __future__ import annotations
from typing import List


class AliveList(List["Animal"]):
    def __repr__(self) -> str:
        return "[" + ", ".join(
            f"{{Name: {a.name}, Health: {a.health}, Hidden: {a.hidden}}}"
            for a in self
        ) + "]"


class Animal:
    alive: AliveList = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _die_check(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            self.health = 0
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other._die_check()
