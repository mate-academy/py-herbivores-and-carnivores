from typing import Callable


class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " f"{self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}" "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Callable) -> None:
        if isinstance(other, Carnivore):
            pass
        elif other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
        else:
            pass
