from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health

        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    @property
    def health(
        self
    ) -> int:
        return self._health

    @health.setter
    def health(
            self,
            value: int
    ) -> None:
        if value < 0:
            value = 0
        self._health = value
        if self._health == 0:
            self.die()

    def die(
            self
    ) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(
            self
    ) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(
            other: Animal
    ) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
