from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in Animal.alive])

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def reduce_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.reduce_health(50)
