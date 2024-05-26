from __future__ import annotations


class Animal:
    alive = []
    health = 100
    hidden = False

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.alive.append(self)
        self.health = health

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health = herbivore.health - 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
