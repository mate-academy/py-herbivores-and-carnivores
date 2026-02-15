from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health : int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)
        else:
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore):
            if not victim.hidden :
                victim.health = max(victim.health - 50, 0)
