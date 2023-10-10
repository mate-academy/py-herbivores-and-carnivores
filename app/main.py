from __future__ import annotations

class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
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


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herb: Herbivore) -> None:
        if isinstance(herb, Herbivore) and herb.hidden is False:
            herb.health -= 50
        if herb.health <= 0:
            Animal.alive.pop(Animal.alive.index(herb))
