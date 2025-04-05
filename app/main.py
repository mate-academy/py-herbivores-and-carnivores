from __future__ import annotations
from typing import List


class Animal:
    alive: List[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        if self.health > 0:
            Animal.alive.append(self)

    def _check_health(self):
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other._check_health()



lion = Carnivore("Simba")
assert len(Animal.alive) == 1
assert isinstance(Animal.alive[0], Carnivore)

rabbit = Herbivore("Susan")
rabbit.hide()
assert rabbit.hidden is True

lion.bite(rabbit)
assert rabbit.health == 100

rabbit.hide()
lion.bite(rabbit)
assert rabbit.health == 50

rabbit.hide()
lion.bite(rabbit)
assert rabbit.health == 50

rabbit.hide()
lion.bite(rabbit)
assert rabbit.health == 0
assert rabbit not in Animal.alive

pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)

