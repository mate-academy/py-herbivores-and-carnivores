from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def check_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def decrease_health(self, amount: int) -> None:
        self.health -= amount
        self.check_alive()


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle the hidden status."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        """Bite a herbivore, decreasing its health if it's not hidden."""
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.decrease_health(50)
