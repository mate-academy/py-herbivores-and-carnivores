from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def died(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: \
{self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    hidden = False

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Carnivore | Herbivore) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50

            if animal.health <= 0:
                animal.died()
