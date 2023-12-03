from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}"
                f"}}")

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.die()
