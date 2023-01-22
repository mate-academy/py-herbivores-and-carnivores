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
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other_animal: Animal) -> None:
        if isinstance(other_animal,
                      Herbivore) and other_animal.hidden is False:
            other_animal.health -= 50
        if other_animal.health <= 0:
            Animal.alive.remove(other_animal)
