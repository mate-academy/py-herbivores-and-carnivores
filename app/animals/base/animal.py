from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = False

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
        self._health = value

        if value <= 0:
            self._health = 0
            self.dead()

    def dead(
        self
    ) -> None:
        Animal.alive.remove(self)

    def __repr__(
        self
    ) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )
