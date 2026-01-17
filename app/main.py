from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if (
            self.health > 0
            and self not in Animal.alive
        ):
            Animal.alive.append(self)

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
    def bite(
        animal: Herbivore
    ) -> None:
        if (
            isinstance(animal, Herbivore)
            and animal.hidden is False
            and animal.health > 0
        ):
            animal.health -= 50

        if (
            isinstance(animal, Herbivore)
            and animal in Animal.alive
            and animal.health <= 0
        ):
            Animal.alive.remove(animal)
