from typing import Any


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    @property
    def health(self) -> Any:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> Any:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: "
                f"{self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Any) -> None:
        if isinstance(other, Carnivore):
            return
        if isinstance(other, Herbivore) and other.hidden:
            return
        if isinstance(other, Herbivore):
            other.health -= 50
