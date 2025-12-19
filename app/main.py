from typing import Any, List


class Animal:
    alive: List["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name: str = name
        self.hidden: bool = False
        self.health: int = health

        if self.health > 0:
            Animal.alive.append(self)

    def __setattr__(
            self,
            key: str,
            value: Any
    ) -> None:
        if key == "health":
            value = max(0, value)

        object.__setattr__(self, key, value)

        if key == "health" and value == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            animal: Animal
    ) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
