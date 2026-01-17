class Animal:
    alive = []  # Revert to a class attribute.

    def __init__(self, name: str, health: int = 100) -> None:
        """Initialize an Animal instance."""
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        acw = self.hidden
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {acw}}}"

    @staticmethod
    def __str__() -> str:
        return "[" + ", ".join(repr(animal) for animal in Animal.alive) + "]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
