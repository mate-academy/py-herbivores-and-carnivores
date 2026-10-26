from __future__ import annotations


class AliveList(list):
    def __repr__(self) -> str:
        items_str = ", ".join(
            f"{{Name: {animal.name}, Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        )
        return f"[{items_str}]"


class AnimalMeta(type):
    @property
    def alive(cls) -> AliveList:
        if not hasattr(cls, "_alive"):
            cls._alive = AliveList()
        return cls._alive

    @alive.setter
    def alive(cls, value: list[Animal]) -> None:
        cls._alive = AliveList(value)


class Animal(metaclass=AnimalMeta):
    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        if self not in Animal.alive:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
