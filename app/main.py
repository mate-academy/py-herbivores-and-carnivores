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
        return f"{{" \
               f"Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50

        other.health = max(0, other.health)

        if other.health == 0:
            Animal.alive.remove(other)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden
