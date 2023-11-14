from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    @classmethod
    def die(cls, herbivore: Herbivore) -> None:
        if herbivore in cls.alive:
            cls.alive.remove(herbivore)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if not isinstance(animal, Herbivore) or animal.hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            Animal.die(animal)
