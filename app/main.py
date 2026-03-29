class Animal:
    alive: list = []

    def __init__(
        self: "Animal",
        name: str,
        health: int = 100
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)
        self._check_alive()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
        )

    def _check_alive(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self: "Herbivore") -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self: "Carnivore",
        other: Animal
    ) -> None:
        if not isinstance(other, Herbivore):
            return

        if other.hidden:
            return

        other.health -= 50

        if other.health < 0:
            other.health = 0

        other._check_alive()

