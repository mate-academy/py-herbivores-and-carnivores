from __future__ import annotations


class AliveList(list):
    """
    A custom list class that provides a specific string representation
    """

    def __repr__(self) -> str:
        """
        Returns the custom string representation of the list.
        """
        formatted_animals = ", ".join(repr(animal) for animal in self)
        return f"[{formatted_animals}]"


class Animal:
    """Represents an animal with health, name, and hidden status."""

    alive: AliveList = AliveList()

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
        animal.health = max(0, animal.health)

        if animal.health == 0:
            Animal.alive.remove(animal)
