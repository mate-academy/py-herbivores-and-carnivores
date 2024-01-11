from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hide: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hide
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
            f"Health: {self.health}, Hidden: {self.hidden}}}"


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
