from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __setattr__(self, attr: str, value: int) -> None:
        if attr == "health" and value <= 0 and self in Animal.alive:
            Animal.alive.remove(self)
        super().__setattr__(attr, value)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                f"}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
