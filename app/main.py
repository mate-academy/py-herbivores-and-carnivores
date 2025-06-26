from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def kill(cls, animal: Animal) -> None:
        if animal in cls.alive:
            cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (
            not isinstance(herbivore, Herbivore)
            or herbivore.hidden
        ):
            return

        herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.kill(herbivore)
