from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive = True

        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                      f"Health: {self.health}, "
                      f"Hidden: {self.hidden}}}")


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (not herbivore.hidden
                and not isinstance(herbivore, Carnivore)):
            if 50 >= herbivore.health > 0:
                Animal.alive.remove(herbivore)
            herbivore.health -= 50


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
