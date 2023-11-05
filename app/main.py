from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.alive.append(self)
        self.health = health
        self.hidden = False

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        text_of_dict = f"Name: {name}, Health: {health}, Hidden: {hidden}"
        return "{" + text_of_dict + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50

        if animal.health <= 0:
            Animal.alive.remove(animal)
