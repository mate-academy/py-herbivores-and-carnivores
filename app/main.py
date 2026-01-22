from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

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
    def bite(self, prey: Herbivore) -> None:
        if prey.hidden:
            return

        prey.health -= 50

        if prey.health <= 0:
            prey.health = 0
            if prey in Animal.alive:
                Animal.alive.remove(prey)
