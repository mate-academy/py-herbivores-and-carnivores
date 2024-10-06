from __future__ import annotations


class Animal:
    alive: [Animal] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + (f"Name: {self.name}, "
                      f"Health: {self.health}, "
                      f"Hidden: {self.hidden}") + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0 and animal in Animal.alive:
                Animal.alive.pop(Animal.alive.index(animal))
