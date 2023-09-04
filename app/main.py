from __future__ import annotations


class Animal:
    alive: list = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        self.alive.append(self)

    def __repr__(self) -> str:
        return ", ".join([
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        ])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, beast: Animal) -> None:
        if not beast.hidden and isinstance(beast, Herbivore):
            beast.health = beast.health - 50
            if beast.health <= 0:
                super().alive.remove(beast)
