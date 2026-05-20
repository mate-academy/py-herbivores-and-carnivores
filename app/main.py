class AliveList(list):
    """Custom list to provide a pretty string representation."""

    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive: list["Animal"] = AliveList()

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

        if self.health <= 0:
            self.health = 0
            self._die()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def clear_alive(cls) -> None:
        """Reset alive animals list."""
        cls.alive.clear()

    def _die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        if herbivore.hidden:
            return

        herbivore.health = max(0, herbivore.health - 50)

        if herbivore.health == 0:
            herbivore._die()


# Example usage
if __name__ == "__main__":
    Animal.clear_alive()

    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan", 25)

    print(Animal.alive)

    lion.bite(rabbit)

    print(rabbit.health)  # 0
    print(Animal.alive)
