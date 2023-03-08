from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False)\
            -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + "Name: " + self.name + ", Health: " + \
            str(self.health) + ", Hidden: " + str(self.hidden) + "}"

    def dead(self) -> None:
        self.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other_animal: Animal) -> None:
        if not isinstance(other_animal, Carnivore) and not other_animal.hidden:
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.dead(other_animal)
