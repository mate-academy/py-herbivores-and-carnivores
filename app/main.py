from __future__ import annotations


class Animal:
    alive: list[Animal] = []

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

    def __repr__(
        self
    ) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, \
Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(
        self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        prey: Herbivore
    ) -> None:
        if isinstance(prey, Herbivore):
            if prey.hidden is False:
                prey.health -= 50
                if prey.health <= 0:
                    remaining_animals = [animal for animal in Animal.alive
                                         if animal != prey]
                    Animal.alive = remaining_animals
