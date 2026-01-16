from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
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
                animal.die()
