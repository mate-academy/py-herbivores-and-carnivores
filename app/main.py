from __future__ import annotations

from typing import ClassVar, List


class AliveList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive: ClassVar[AliveList] = AliveList()

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )

    def _die_if_needed(self) -> None:
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.health -= 50
        other._die_if_needed()
