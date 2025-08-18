from typing import List



class Animal:
    alive: List["Animal"] = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0:
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
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50

        if prey.health <= 0:
            prey.die()
