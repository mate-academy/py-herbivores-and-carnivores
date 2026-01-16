from typing import Any


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False, *args: Any) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __str__(self) -> str:
        return str([repr(animal) for animal in Animal.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if (isinstance(prey, Herbivore)
                and not prey.hidden
                and prey in Animal.alive):
            prey.health -= 50
            if prey.health <= 0:
                prey.die()
