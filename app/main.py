from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(
        self: "Animal",
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def take_damage(
        self: "Animal",
        amount: int,
    ) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(
        self: "Animal",
    ) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(
        self: "Herbivore",
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self: "Carnivore",
        other: Animal,
    ) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.take_damage(50)
