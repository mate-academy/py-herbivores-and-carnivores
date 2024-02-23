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
        self.add_to_alive()

    def add_to_alive(self) -> None:
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbi: Herbivore) -> None:
        if isinstance(herbi, Herbivore) and not herbi.hidden:
            herbi.health -= 50
            if herbi.health <= 0:
                Animal.alive.remove(herbi)
