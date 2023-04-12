from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> dict:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def take_damage(self, damage_rate: int) -> None:
        if self.hidden:
            return

        self.health -= damage_rate

        if self.health <= 0:
            self.die()  # Rest in Peace, little one ='(

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    damage_rate = 50

    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        herbivore.take_damage(self.damage_rate)
