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

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = not self.hidden
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore | Carnivore) -> None:
        if not isinstance(animal, Carnivore) and animal.hidden is False:
            animal.health -= 50

        if animal.health <= 0:
            Animal.alive.remove(animal)
