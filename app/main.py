from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
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


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Carnivore):
            if not herbivore.hidden:
                herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
