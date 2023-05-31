
from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str,
                 health: int = 100,
                 is_hidden: bool = False) -> None:
        self._name: str = name
        self._hidden: bool = is_hidden
        self._health: int = health
        Animal.alive.append(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def hidden(self) -> bool:
        return self._hidden

    @property
    def health(self) -> int:
        return self._health

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @property
    def is_alive(self) -> bool:
        return self in Animal.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self._hidden = not self._hidden

    def recieve_damage(self, value: int) -> None:
        if not self.is_alive:
            return
        self._health -= value
        if self._health < 1:
            Animal.alive.remove(self)


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.recieve_damage(50)
