from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> Herbivore:
        self.hidden = not self.hidden
        return self


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> str:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden:
                return f"{self.name} cannot bite hidden {herbivore.name}"

            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                Animal.alive.remove(herbivore)
