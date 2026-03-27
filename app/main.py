from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return str(cls.alive)

    def take_damage(self, amount: int) -> None:
        """Зменшує здоров'я та видаляє тварину з alive, якщо воно ≤ 0."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.take_damage(50)
