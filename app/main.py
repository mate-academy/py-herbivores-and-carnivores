from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False

        if self.health > 0:
            Animal.alive.append(self)

    def take_damage(
        self,
        damage: int,
    ) -> None:
        if self.health <= 0:
            return

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(
        self,
    ) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(
        self,
    ) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(
        self,
    ) -> None:
        if self.health > 0:
            self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        other: Animal,
    ) -> None:
        if self.health <= 0:
            return
        if isinstance(other, Carnivore):
            return
        if other.hidden:
            return
        if other.health > 0:
            other.take_damage(50)
