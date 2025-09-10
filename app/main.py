from typing import Any


class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(
        self,
    ) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(
        self,
    ) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(
        self,
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        beast: Any,
    ) -> None:
        if isinstance(beast, Herbivore) and not beast.hidden:
            beast.health -= 50
            if beast.health <= 0:
                beast.health = 0
                beast.die()
