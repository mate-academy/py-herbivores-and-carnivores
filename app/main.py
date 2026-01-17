from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(week_animal: Herbivore) -> None:
        if isinstance(week_animal, Herbivore) and week_animal.hidden is False:
            week_animal.health -= 50
        if week_animal.health <= 0:
            Animal.alive.remove(week_animal)
