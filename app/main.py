from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            *args
    ) -> None:
        self.name = name
        self.health = 100
        if any(args):
            self.health = args[0]
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(
            self
    ) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self,
            prey: Herbivore
    ) -> None:
        if prey.hidden is False and isinstance(prey, Herbivore):
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)
