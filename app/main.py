from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target_herbivore: Herbivore) -> None:
        if (isinstance(target_herbivore, Herbivore)
           and target_herbivore.hidden is False):

            target_herbivore.take_damage(50)
