from __future__ import annotations


class AliveList(list):
    def __repr__(self) -> str:
        animals = (
            f"{{Name: {animal.name}, "
            f"Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        )
        return f"[{', '.join(animals)}]"


class Animal:
    alive: AliveList = AliveList()

    def __init__(
        self,
        name: str,
        health: int = 100,
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

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
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        victim: Animal,
    ) -> None:
        if (
            isinstance(victim, Herbivore)
            and not victim.hidden
            and victim.health > 0
        ):
            victim.health -= 50
            if victim.health <= 0:
                victim.health = 0
                victim.die()
