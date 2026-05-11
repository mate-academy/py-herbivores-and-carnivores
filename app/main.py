from __future__ import annotations


class Animal:

    alive: list = []

    def __init__(
        self, name: str,
        health: int | None = None,
        hidden: bool | None = None
    ) -> None:
        self.name = name
        self.health = health or 100
        self.hidden = hidden or False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        self.health = 0
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def is_valid_target(herbivore: Herbivore) -> bool:
        return (
            isinstance(herbivore, Herbivore)
            and not herbivore.hidden
            and herbivore.health > 0
        )

    def bite(self, herbivore: Herbivore) -> None:
        if Carnivore.is_valid_target(herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
