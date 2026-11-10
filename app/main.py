from __future__ import annotations
from typing import ClassVar


class AliveList(list):
    def __repr__(self) -> str:
        items = [
            f"{{Name: {animal.name}, Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        ]
        return f"[{', '.join(items)}]"


class Animal:
    alive: ClassVar[AliveList] = AliveList()

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self._health = max(0, health)
        self.hidden = hidden

        if self not in Animal.alive:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"Animal(name={self.name!r}, health={self.health}, "
            f"hidden={self.hidden})"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden or target.health == 0:
            return
        target.health -= 50
