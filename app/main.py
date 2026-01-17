from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """Return formatted string representation for alive animals."""
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def check_health(self) -> None:
        """Remove animal from alive list if health <= 0."""
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle hidden status."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        other: Animal,
    ) -> None:
        """Bite herbivore if visible."""
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health < 0:
            other.health = 0
        other.check_health()
