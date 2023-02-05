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
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> Herbivore:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
        return self


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:

        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50

        if other.health <= 0:
            for index, animal in enumerate(Animal.alive):
                if animal == other:
                    Animal.alive.pop(index)
