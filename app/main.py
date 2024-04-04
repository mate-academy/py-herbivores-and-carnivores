from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{self.__dict__}".replace("'", "").title()

    def death(self) -> None:
        if self.health <= 0:
            self.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):

    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        prey.death()
