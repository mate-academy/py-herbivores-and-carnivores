from __future__ import annotations

from typing import ClassVar, List


class Animal:
    alive: ClassVar[List["Animal"]] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self._health = 100
        self.health = health
        if self.health > 0:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, int(value))
        if self._health == 0:
            self._remove_from_alive()

    def _remove_from_alive(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        if animal.health == 0:
            return

        animal.health -= 50
