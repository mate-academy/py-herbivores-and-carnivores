from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)
        self.check_alive(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @staticmethod
    def check_alive(animal: Animal) -> None:
        if animal.health <= 0:
            Animal.alive.remove(animal)


class Herbivore(Animal):
    @staticmethod
    def hide() -> None:
        for animal in Animal.alive:
            animal.hidden = not animal.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if not animal.hidden and not isinstance(animal, Carnivore):
            animal.health -= 50
        Animal.check_alive(animal)
