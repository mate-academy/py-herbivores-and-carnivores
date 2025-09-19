from typing import List


class Animal:
    """Base class for all animals."""

    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Initialize animal with default attributes.

        Args:
            name: The name of the animal.
            health: Initial health (default 100).
        """
        self.name: str = name
        # garante que a vida nunca seja negativa
        self.health: int = max(0, int(health))
        self.hidden: bool = False
        # só entra na lista de vivos se tiver vida > 0
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        """Represent Animal.alive nicely when printed."""
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        """Remove the animal from alive list when health reaches 0."""
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    """Herbivore animal that can hide."""

    def hide(self) -> None:
        """Toggle hidden state to escape carnivores."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """Carnivore animal that can bite herbivores."""

    def bite(self, other: Animal) -> None:
        """Bite a herbivore if conditions allow."""
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other.health = 0  # não deixar negativo
            other.die()
