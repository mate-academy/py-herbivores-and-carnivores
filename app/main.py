from typing import ClassVar


class Animal:
    """Base class for all animals in the ecosystem."""

    alive: ClassVar[list["Animal"]] = []

    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def _check_death(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    @staticmethod
    def print_alive() -> None:
        print([repr(animal) for animal in Animal.alive])


class Herbivore(Animal):
    """Herbivore that can hide from carnivores."""

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    """Carnivore that can bite herbivores."""

    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()
