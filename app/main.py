from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @staticmethod
    def remove_animal(animal: "Animal") -> None:
        Animal.alive.remove(animal)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return Animal.__str__(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: "Herbivore") -> None:
        if animal.hidden or isinstance(animal, Carnivore):
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.remove_animal(animal)
