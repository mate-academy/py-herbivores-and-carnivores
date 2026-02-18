from typing import List, Union


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        if health < 0:
            raise ValueError("Health cannot be negative")

        self.name: str = name
        self.health: int = health
        self.hidden: bool = False

        if self.health > 0:
            Animal.alive.append(self)

    def _check_health(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

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
    def bite(self, target: Union[Herbivore, Animal]) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_health()
