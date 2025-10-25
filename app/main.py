from __future__ import annotations
from typing import Optional


class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: Optional[str] = None,
                 health: int = 100,
                 hidden: bool = False,
                 ) -> None:
        self.name = name
        self.hidden = hidden
        # internal storage for health; use property to keep alive in sync
        self._health: int = 0
        self.health = health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        # cast to int to be robust against unexpected numeric types
        self._health = int(value)
        # keep Animal.alive membership consistent and guarded
        if self._health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)
        else:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
