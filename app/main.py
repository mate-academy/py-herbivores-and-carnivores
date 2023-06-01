from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Animal) -> None:
        if not isinstance(victim, Carnivore) and not victim.hidden:
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
