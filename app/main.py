from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return str(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
