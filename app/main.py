from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{" \
               f"Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal) -> None:
        if other.hidden is False and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
