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
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @staticmethod
    def print_alive() -> str:
        return f'[{", ".join(repr(animal) for animal in Animal.alive)}]'


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def die(self) -> None:
        Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50

            if animal.health <= 0:
                animal.die()
