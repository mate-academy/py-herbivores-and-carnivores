from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str, health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivores: Herbivore) -> None:
        if isinstance(herbivores, Herbivore) and not herbivores.hidden:
            herbivores.health -= 50
            if herbivores.health <= 0:
                Animal.alive.remove(herbivores)
