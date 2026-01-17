from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:

        self.health = health
        self.name = name
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: "Herbivore") -> None:
        if not isinstance(prey, Herbivore) or prey.hidden or prey.health <= 0:
            return
        prey.health = max(prey.health - 50, 0)
        if prey.health == 0:
            prey.die()
