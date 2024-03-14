from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> bool:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, animal: Herbivore | Carnivore) -> int | list:
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
        if animal.health <= 0:
            self.alive.remove(animal)
