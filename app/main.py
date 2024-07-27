from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if not isinstance(other, Carnivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
