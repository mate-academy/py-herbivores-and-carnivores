from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int | float = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def update_alive(cls, died_animal: Animal) -> None:
        cls.alive = [
            animal
            for animal in cls.alive
            if animal.name != died_animal.name
        ]

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def die(self) -> None:
        Animal.update_alive(self)


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50

            if victim.health <= 0:
                victim.die()
