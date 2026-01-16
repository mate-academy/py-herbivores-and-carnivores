from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def die(self) -> None:
        """Remove the animal from the alive list."""
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        """Return a readable representation of the animal."""
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle hidden state."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        """Decrease herbivore’s health by 50 if visible."""
        if not isinstance(prey, Herbivore):
            return
        if prey.hidden:
            return

        prey.health -= 50
        if prey.health <= 0:
            prey.health = 0
            prey.die()
