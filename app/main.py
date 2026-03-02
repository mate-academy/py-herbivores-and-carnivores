from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.add_to_alive(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def add_to_alive(cls, animal: Animal) -> None:
        cls.alive.append(animal)

    @classmethod
    def remove_from_alive(cls, animal: Animal) -> None:
        cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (isinstance(herbivore, Herbivore)
                and herbivore.hidden is False
                and herbivore in Animal.alive):
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.remove_from_alive(herbivore)
