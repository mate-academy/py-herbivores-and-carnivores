from typing import List, Union


class Animal:
    """Base Animal class with shared attributes for all animals."""
    alive: List["Animal"] = []  # List of all alive animals

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)  # Add the animal to the alive list

    def __repr__(self) -> str:
        """Return a string representation of alive animals."""
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def remove_dead(cls, animal: "Animal") -> None:
        """Remove animal from alive list if its health reaches 0."""
        if animal in cls.alive:
            cls.alive.remove(animal)


class Herbivore(Animal):

    def hide(self) -> None:
        """Toggle the hidden attribute."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """Carnivore class inherits from Animal and can bite herbivores."""

    def bite(self, other: Union[Herbivore, "Carnivore"]) -> None:
        """Bite a herbivore and reduce its health by 50.

        Does nothing if the other animal is a carnivore or if
        the herbivore is hiding.
        """
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.remove_dead(other)
