from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __setattr__(self, name: str, value: int | bool | str) -> None:
        super().__setattr__(name, value)
        if name == "health" and value <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
