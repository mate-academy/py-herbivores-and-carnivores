class Animal:
    alive: list = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.hidden: bool = False
        Animal.alive.append(self)
        self._health: int = health

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0:
            self._health = 0
            self.die()

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
