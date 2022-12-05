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
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {False}}}"

    def __sub__(self, other: Animal) -> Animal:
        self.health -= other.health
        return Animal(self.name, self.health, self.hidden)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is self.hidden:
            self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Carnivore) or animal.hidden is True:
            pass
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
