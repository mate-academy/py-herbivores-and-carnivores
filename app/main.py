from __future__ import annotations


class Animal:

    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " + str(self.name)
            + ", Health: " + str(self.health)
            + ", Hidden: " + str(self.hidden) + "}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:

        if not isinstance(herbivore, Herbivore):
            return

        if not herbivore.hidden:
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
