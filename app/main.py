from typing import Any, List


class AliveList(list):
    """Custom list class to format the print output of Animal.alive."""

    def __repr__(self) -> str:
        items_repr = [
            f"{{Name: {animal.name}, Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        ]
        return "[" + ", ".join(items_repr) + "]"


class MetaAnimal(type):
    """Metaclass to ensure Animal.alive always stays an AliveList."""

    @property
    def alive(cls) -> AliveList:
        if not hasattr(cls, "_alive"):
            cls._alive = AliveList()
        return cls._alive

    @alive.setter
    def alive(cls, value: List[Any]) -> None:
        if not hasattr(cls, "_alive"):
            cls._alive = AliveList()
        else:
            cls._alive.clear()
        cls._alive.extend(value)


class Animal(metaclass=MetaAnimal):
    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self._health: int = health
        self.hidden: bool = False
        if self._health > 0:
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
        if isinstance(other, Carnivore):
            return
        if isinstance(other, Herbivore) and other.hidden:
            return
        if other in Animal.alive and other.health > 0:
            other.health -= 50
