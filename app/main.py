from typing import Any


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}, Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"

    def check_fall(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Any) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
            other.check_fall()
