from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def __sub__(animal: Animal) -> Animal:
        if not animal.hidden:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
        return animal


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            Animal.__sub__(animal)
