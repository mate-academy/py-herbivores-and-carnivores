from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"  # opening brace
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )


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
        if target.health == 0:
            return
        target.health = max(target.health - 50, 0)
        if target.health == 0 and target in Animal.alive:
            Animal.alive.remove(target)
