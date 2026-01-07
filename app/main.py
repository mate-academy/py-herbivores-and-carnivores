from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)
        if self._health <= 0:
            Animal.alive.remove(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(
        self,
        value: int
    ) -> None:
        self._health = value
        if self in Animal.alive and self._health <= 0:
            Animal.alive.remove(self)

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
    def bite(
        self,
        target: "Animal"
    ) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
