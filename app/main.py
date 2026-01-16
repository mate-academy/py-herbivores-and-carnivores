from __future__ import annotations


class Animal:
    class AliveList(list):
        def __str__(self) -> str:
            return f'[{", ".join(repr(a) for a in self)}]'

    alive = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def _remove_if_dead(cls, animal: Animal) -> None:
        if animal.health <= 0 and animal in cls.alive:
            cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if (
            isinstance(other, Herbivore)
            and not other.hidden
            and other.health > 0
        ):
            other.health -= 50
        Animal._remove_if_dead(other)
