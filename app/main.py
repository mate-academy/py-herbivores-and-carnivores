from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self,
        name: str
    ) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return str(self)

    def _die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        target: Animal
    ) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target._die()
