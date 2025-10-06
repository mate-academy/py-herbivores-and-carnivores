from typing import List, Any


class Animal:
    alive: List[Any] = []

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
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _check_health(self) -> None:
        """Check if animal is dead and remove from alive list if necessary."""
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle the hidden attribute."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        """Bite another animal - only works on unhidden herbivores."""
        # Check if other is a herbivore and not hidden
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other._check_health()  # Check if herbivore died
