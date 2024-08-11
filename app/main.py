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

    @classmethod
    def is_alive(cls, animal: Animal) -> None:
        if animal.health <= 0:
            cls.alive.remove(animal)

    def __repr__(self) -> str:
        return "{" + (f"Name: {self.name}, "
                      f"Health: {self.health}, "
                      f"Hidden: {self.hidden}") + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if not prey.hidden and isinstance(prey, Herbivore):
            prey.health -= 50
        Animal.is_alive(prey)
