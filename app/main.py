from __future__ import annotations


class Animal:
    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, "  \
               f"Health: {self.health}, "  \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, animal: Herbivore | Carnivore) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
