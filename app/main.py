from __future__ import annotations


class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal_herbivore: Herbivore) -> None:
        if (
            isinstance(animal_herbivore, Herbivore)
            and not animal_herbivore.hidden
        ):
            animal_herbivore.health -= 50

        index = cls.alive.index(animal_herbivore)
        if animal_herbivore.health <= 0:
            del cls.alive[index]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
