"""Domain models for the herbivores and carnivores simulation."""


class Animal:
    """Base class for every creature living in Animal.alive."""

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        """Return a readable card, e.g. {Name: Kaa, Health: 100, ...}."""
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        """Remove this animal from the list of the living."""
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    """A peaceful animal that can hide from predators."""

    def hide(self) -> None:
        """Toggle hidden state — hide from or reveal to carnivores."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """A predator that can bite herbivores."""

    def bite(self, target: Animal) -> None:
        """Bite a target, reducing its health by 50.

        Does nothing if the target is another carnivore or if the
        target is currently hidden.
        """
        if isinstance(target, Carnivore):
            return
        if target.hidden:
            return

        target.health -= 50
        if target.health <= 0:
            target.health = 0
            target.die()
