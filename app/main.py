from __future__ import annotations


class AnimalList(list):
    def __repr__(self) -> str:
        return f"[{', '.join(map(repr, self))}]"


class Animal:
    alive: AnimalList = AnimalList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50

            if animal.health <= 0:
                Animal.alive.remove(animal)
