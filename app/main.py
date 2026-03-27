from __future__ import annotations
from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        # приводим к int и не даём уйти ниже 0
        self.health: int = max(0, int(health))
        self.hidden: bool = False

        # добавляем в список живых только если здоровье > 0
        if self.health > 0:
            Animal.alive.append(self)

    def die(self) -> None:
        """Если здоровье <= 0 — фиксируем 0 и удаляем из живых."""
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        # у списков используется __repr__ элементов
        return (
            "{Name: "
            f"{self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        # кусаем только травоядных и только если они не спрятаны
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.die()
