# write your code here
from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        # cannot bite non-herbivores
        if not isinstance(animal, Herbivore):
            return

        # cannot bite hidden herbivores
        if animal.hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()
