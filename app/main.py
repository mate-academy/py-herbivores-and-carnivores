from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int | float = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def remove_from_alive(cls, animal: Herbivore) -> None:
        if animal.health <= 0:
            cls.alive.remove(animal)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, victim: Herbivore) -> None:
        if (
            not isinstance(victim, Carnivore)
            and victim.hidden is not True
        ):
            victim.health -= 50
            Animal.remove_from_alive(victim)
