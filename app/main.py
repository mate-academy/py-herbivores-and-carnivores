from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self._health = health
        self.name = name
        self.hidden = hidden
        if self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(
            self
    ) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

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
        if value <= 0:
            self._health = 0
            self.die()
        else:
            self._health = value


class Herbivore(Animal):
    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            other: Animal
    ) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
