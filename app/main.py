from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def remove_dead(target: Animal) -> None:
        if target.health <= 0 and target in Animal.alive:
            Animal.alive.remove(target)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if (
            isinstance(target, Herbivore)
            and not target.hidden
        ):
            target.health -= 50
            Animal.remove_dead(target)
