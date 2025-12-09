from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):
    def bite(self, herb: Herbivore) -> None:
        if isinstance(herb, Herbivore) and not herb.hidden:
            herb.health -= 50
            if herb.health <= 0 and herb in Animal.alive:
                Animal.alive.remove(herb)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
