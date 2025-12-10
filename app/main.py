from __future__ import annotations
from typing import Any, List


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        # Add to alive list first
        Animal.alive.append(self)

        # If created dead → remove immediately
        if self.health <= 0:
            self.die()

    def __setattr__(
        self,
        key: str,
        value: Any,
    ) -> None:
        if key == "health" and hasattr(self, "health"):
            super().__setattr__(key, value)
            if value <= 0:
                self.die()
            return

        super().__setattr__(key, value)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        target: Animal,
    ) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return

        target.health -= 50
