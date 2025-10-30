from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
