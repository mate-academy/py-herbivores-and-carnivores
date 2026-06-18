from __future__ import annotations


class AliveAnimals(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive: AliveAnimals = AliveAnimals()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

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
    def bite(self, herbivore: Animal) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        if herbivore.hidden:
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            herbivore.health = 0

            if herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
