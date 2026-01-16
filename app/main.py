from typing import Any


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            + f"Health: {self.health}, Hidden: {self.hidden}}}"
        )

    def __str__(self) -> str:
        return (
            "[" + ", ".join(repr(instance) for instance in Animal.alive) + "]"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Any) -> None:
        print(f"{self.name} bite {animal.name}")
        if animal in Animal.alive and isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
        else:
            print(f"{self.name} cannot bite because they dead")
