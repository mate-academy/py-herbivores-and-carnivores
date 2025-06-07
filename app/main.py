from typing import ClassVar, List


class Animal:
    alive: ClassVar[List["Animal"]] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)
        self._check_health()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _check_health(self) -> None:
        if self.health <= 0 and self in Animal.alive:
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
        target._check_health()
