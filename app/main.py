from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)
