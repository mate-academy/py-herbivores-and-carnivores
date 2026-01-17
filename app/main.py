from __future__ import annotations


class Animal:
    alive = []

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.health -= 50
        if target.health <= 0 and target in Animal.alive:
            Animal.alive.remove(target)
