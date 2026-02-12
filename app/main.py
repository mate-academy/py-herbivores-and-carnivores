class Animal:
    # Class attribute to track all instances
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        # Automatically add to the tracking list upon creation
        Animal.alive.append(self)

    def _check_death(self) -> None:
        """Internal helper to clean up Animal.alive if health drops to 0."""
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        """Format output to fit within a 79-character line limit."""
        parts = [
            f"{{Name: {self.name}",
            f"Health: {self.health}",
            f"Hidden: {self.hidden}}}"
        ]
        return ", ".join(parts)


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggles the hidden state."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        """
        Reduces target health by 50 if target is a visible Herbivore.
        """
        # Logic check: Must be Herbivore and not hidden
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()
