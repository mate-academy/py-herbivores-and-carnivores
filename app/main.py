from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def die_if_needed(self) -> None:
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.health = max(0, other.health - 50)
        other.die_if_needed()
