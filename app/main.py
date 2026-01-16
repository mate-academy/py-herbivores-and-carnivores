from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def death(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    @property
    def health(self) -> Animal:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        if value <= 0:
            self._health = 0
            self.death()
        else:
            self._health = value

    def __repr__(self) -> None:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                f"}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
