from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: "Animal") -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                if other.health > 0:
                    other.health -= 50
                    if other.health <= 0:
                        if other in Animal.alive:
                            Animal.alive.remove(other)
