from typing import Any


class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __setattr__(self, key: str, value: Any) -> None:
        object.__setattr__(self, key, value)
        if key == "health" and value <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    @classmethod
    def get_alive(cls) -> str:
        result = []
        for animal in cls.alive:
            result.append(
                f"{{Name: {animal.name}, Health: {animal.health}, "
                f"Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(result) + "]"

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
