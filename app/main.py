from __future__ import annotations


class AnimalList(list):
    def __str__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive: AnimalList = AnimalList()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0:
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
    def bite(
            self,
            other_animal: Herbivore,
    ) -> None:
        if (
            not other_animal.hidden
            and isinstance(other_animal, Herbivore)
        ):
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)
