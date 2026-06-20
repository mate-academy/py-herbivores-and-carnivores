from __future__ import annotations


class AliveList(list):
    def __repr__(self) -> str:
        result = []
        for animal in self:
            current = (
                f"{{Name: {animal.name}, "
                f"Health: {animal.health}, "
                f"Hidden: {animal.hidden}}}"
            )
            result.append(current)
        return f"[{', '.join(result)}]"


class Animal:
    alive = AliveList()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive = AliveList(Animal.alive)
        Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if not isinstance(other, Carnivore):
            if not other.hidden:
                other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
