from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Animal:
    name: str
    health: int = 100
    hidden: bool = False

    alive: ClassVar[list[Animal]] = []

    def __post_init__(self) -> None:
        Animal.alive.append(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
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
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.take_damage(50)
