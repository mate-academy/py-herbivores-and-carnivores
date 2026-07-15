from __future__ import annotations


class Animal:
    alive: list[Animal] = []

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

    def was_bitten(self) -> None:
        self.health -= 50

    @staticmethod
    def handle_death(target: Animal) -> None:
        """Removes instance from the list."""
        Animal.alive.remove(target)

    def __repr__(self) -> str:
        """User-friendly representation for print()."""
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):

    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            return

        target.was_bitten()

        if target.health <= 0:
            target.handle_death(target)


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggles the hidden state of the herbivore."""
        self.hidden = not self.hidden
