from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def print_alive(cls) -> list[str]:
        return [str(animal) for animal in cls.alive]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                other.health = 0
                other.die()
