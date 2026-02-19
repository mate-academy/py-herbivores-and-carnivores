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
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        self.update_life_status()

    def update_life_status(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        info = (
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
        )
        return f"{{{info}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.health -= 50
        target.update_life_status()


def bite(target: Herbivore) -> None:
    for animal in Animal.alive:
        if isinstance(animal, Carnivore):
            animal.bite(target)
            break
