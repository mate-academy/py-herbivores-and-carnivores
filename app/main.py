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
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore_animal: Herbivore) -> None:
        if isinstance(herbivore_animal, Herbivore)\
                and herbivore_animal.hidden is False:
            herbivore_animal.health -= 50
            if herbivore_animal.health <= 0:
                index = Animal.alive.index(herbivore_animal)
                Animal.alive.pop(index)
