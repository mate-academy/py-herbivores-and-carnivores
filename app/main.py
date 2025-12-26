from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    @classmethod
    def change_alive(cls, obj: Animal) -> None:
        if obj in cls.alive:
            cls.alive.remove(obj)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if other.health <= 0:
            Animal.change_alive(other)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
