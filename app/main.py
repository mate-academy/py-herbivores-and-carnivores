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
        Animal.add_to_alive(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def add_to_alive(cls, creature: Animal) -> None:
        if creature.health > 0:
            cls.alive.append(creature)

    def check_health(self) -> None:
        if self.health <= 0:
            self.remove_from_alive()

    def remove_from_alive(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(creature: Herbivore) -> None:
        if not isinstance(creature, Carnivore) and not creature.hidden:
            creature.health -= 50
            creature.check_health()
