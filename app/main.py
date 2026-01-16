from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore) or target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            Animal.alive.remove(target)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
