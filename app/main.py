from __future__ import annotations
from typing import List, Union


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if self.health > 0:
            Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        self.die()

    def __repr__(self) -> str:
       return (
           f"{{"
           f"Name: {self.name}, "
           f"Health: {self.health}, "
           f"Hidden: {self.hidden}}}"
       )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Union[Herbivore, Animal]) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)
