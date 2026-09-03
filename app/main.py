from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

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
        if animal.hidden or not isinstance(animal, Herbivore):
            print(f"{self.name} cannot bite hidden {animal.name}")
        else:
            animal.health -= 50
            print("bited")
            if animal.health <= 0:
                Animal.alive.remove(animal)
                print(f"{animal.name} is dead")
