from __future__ import annotations
from dataclasses import dataclass, field
from typing import ClassVar, List


@dataclass
class Animal:
    name: str
    health: int = 100
    hidden: bool = False

    alive: ClassVar[List["Animal"]] = []

    def __post_init__(self) -> None:
        # Normalize health
        self.health = max(0, self.health)

        if self.health > 0:
            self.__class__.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)
        if self.health == 0:
            self.die()

    def die(self) -> None:
        if self in self.__class__.alive:
            self.__class__.alive.remove(self)

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
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.take_damage(50)
