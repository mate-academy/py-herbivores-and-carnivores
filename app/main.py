from typing import ClassVar


class Animal:
    alive: ClassVar = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.adding_to_alive()

    def adding_to_alive(self) -> None:
        self.alive.append(self)

    @classmethod
    def remove_animal(cls, herbivore_unit: object) -> None:
        cls.alive.remove(herbivore_unit)

    def __repr__(self) -> str:
        prep_msg = "Name: {0}, Health: {1}," \
                   " Hidden: {2}".format(self.name, self.health, self.hidden)
        return f"{{{prep_msg}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health = herbivore.health - 50
            if herbivore.health <= 0:
                Animal.remove_animal(herbivore)
