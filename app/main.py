from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: float | int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def animal_checker() -> None:
        for element in Animal.alive:
            if element.health <= 0:
                Animal.alive.remove(element)
                break


class Herbivore(Animal):

    def hide(self) -> bool:
        if not self.hidden:
            self.hidden = True
            return self.hidden
        self.hidden = False
        return self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50

        Animal.animal_checker()
