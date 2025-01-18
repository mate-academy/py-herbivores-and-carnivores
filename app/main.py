from __future__ import annotations


class Animal:
    alive = []
    health = 100
    hidden = False

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> Herbivore:
        if not isinstance(herbivore, Herbivore) or herbivore.hidden:
            print(f"{self.name} cannot bite hidden {herbivore.name}")
            return herbivore
        if herbivore in Animal.alive:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

        return herbivore
