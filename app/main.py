from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> None:
        return str(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None\
            :
        if isinstance(animal, Carnivore) or animal.hidden:
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
