from typing import Union, List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Union[Animal, object]) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0 and other in Animal.alive:
            Animal.alive.remove(other)
