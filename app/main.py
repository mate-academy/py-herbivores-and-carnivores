from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.hidden = hidden
        self.name = name
        Animal.alive.append(self)

    def __repr__(self) -> str:
        result_strings = (f"{{Name: {self.name}, "
                          f"Health: {self.health}, Hidden: {self.hidden}}}")
        return result_strings


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
