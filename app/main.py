from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str = None, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
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
    def bite(self, other: Herbivore | Carnivore) -> None:
        if other.hidden or isinstance(other, Carnivore):
            pass
        else:
            other.health -= 50

        if other.health <= 0:
            Animal.alive.remove(other)
