from __future__ import annotations


class Animal:
    """Represents an animal with health, name, and hidden status."""

    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        """
        Initializes an Animal instance.
        """
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """Returns the string representation of the Animal instance."""
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    """Represents a herbivore that can hide."""

    def hide(self) -> None:
        """Toggles the hidden status of the herbivore."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """Represents a carnivore that can bite."""

    def bite(
        self,
        animal: Animal
    ) -> None:
        """
        A carnivore bites another animal.
        """
        if animal.hidden or isinstance(animal, Carnivore):
            return

        animal.health -= 50
        # Clamping health to zero
        animal.health = max(0, animal.health)

        if animal.health == 0:
            Animal.alive.remove(animal)
