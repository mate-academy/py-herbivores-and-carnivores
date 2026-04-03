from __future__ import annotations


class Animal:

    alive: list[Animal] = []

    def __init__(
            self, name: str, health:
            int = 100, hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __str__(self) -> str:
        text = str({
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }).replace("'", "")
        return f"{text}"

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other: Herbivore) -> None:
        if not isinstance(other, Carnivore) and not other.hidden:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
