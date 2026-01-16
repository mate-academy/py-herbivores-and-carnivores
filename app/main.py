from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self._health: int = health
        self.name: str = name
        self.hidden: bool = False
        if self._health > 0:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return
        if not animal.hidden:
            animal.health -= 50
