from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.hidden: bool = False
        self._health: int = health

        # Додаємо тварину до списку живих лише якщо її здоров'я більше 0
        if self._health > 0:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self._health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
