from __future__ import annotations


class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, \
            Health: {self.health}, \
            Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
        if animal.health < 1:
            Animal.alive.remove(animal)

