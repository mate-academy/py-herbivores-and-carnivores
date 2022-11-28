from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False

        Animal.alive.append(self)

    @classmethod
    def del_alive_herbivore(cls, herbivore: Herbivore) -> None:
        if herbivore.health <= 0:
            cls.alive.remove(herbivore)

    def __repr__(self) -> str:
        return "{{Name: {}, Health: {}, Hidden: {}}}".format(
            self.name,
            self.health,
            self.hidden
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50

        Animal.del_alive_herbivore(herbivore)
