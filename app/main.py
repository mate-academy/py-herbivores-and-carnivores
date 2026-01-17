from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


def create_animal(alive_list: list) -> list:
    Animal.alive = []
    for beast in alive_list:
        animal = Animal(beast["name"], beast["health"], beast["hidden"])
        Animal.alive.append(animal)
    return Animal.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if (not isinstance(other, Carnivore) and not self.hidden
                and not other.hidden):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
