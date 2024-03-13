from __future__ import annotations


class Animal:
    alive: list[Animal] = []

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


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Animal) -> None:
        if animal.hidden or not animal.health or isinstance(animal, Carnivore):
            return

        animal.health -= min(animal.health, 50)

        if not animal.health:
            Animal.alive.remove(animal)
