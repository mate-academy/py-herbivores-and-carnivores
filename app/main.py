from typing import Any, ClassVar, List


class Animal:
    alive: ClassVar[List["Animal"]] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        if self.health > 0:
            Animal.alive.append(self)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "health":
            value = max(0, value)
            if hasattr(self, "health") and value == 0 and self in Animal.alive:
                Animal.alive.remove(self)
        super().__setattr__(key, value)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
