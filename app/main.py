from __future__ import annotations


class Animal:
    alive = []

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbi: Herbivore) -> None:
        if isinstance(herbi, Herbivore) and not herbi.hidden:
            herbi.health -= 50
            if herbi.health < 1:
                Animal.alive.remove(herbi)
