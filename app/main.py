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

    def __repr__(self) -> str:
        return str(self.__dict__).replace("\'", "").title()

    def death(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Animal) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
        if victim.health <= 0:
            victim.death()
