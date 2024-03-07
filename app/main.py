from typing import List


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

    def die(self) -> None:
        Animal.alive.remove(self)
        del self


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.die()
