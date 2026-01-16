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

    def remove_from_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        name, health, hidden = self.name, self.health, self.hidden
        return (
            f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore | Carnivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.remove_from_alive()
