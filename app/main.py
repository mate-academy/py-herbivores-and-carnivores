from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Carnivore(Animal):

    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        if prey.health <= 0:
            prey.health = 0
            for animal in Animal.alive:
                if animal.name == prey.name:
                    Animal.alive.remove(animal)
                    break


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
