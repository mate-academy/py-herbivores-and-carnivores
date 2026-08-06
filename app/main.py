from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.hidden: bool = False
        self._health: int = 100
        Animal.alive.append(self)
        self.health = health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0:
            self._health = 0
            if self in Animal.alive:
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
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            return

        if target.hidden:
            return

        target.health -= 50
