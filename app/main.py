from __future__ import annotations


class Health:
    def __check(self, result: int) -> None:
        if result <= 0:
            Animal.alive.pop(Animal.alive.index(self.animal))

    def __init__(self, animal: Animal, value: int) -> None:
        self.animal = animal
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __sub__(self, other: Health | int) -> int:
        rvalue = 0
        if isinstance(other, int):
            rvalue = other
        elif isinstance(other, Health):
            rvalue = other.value
        result = self.value - rvalue
        self.__check(result)
        return result

    def __isub__(self, other: Health | int) -> Health:
        if isinstance(other, int):
            self.value -= other
        elif isinstance(other, Health):
            self.value -= other.value
        self.__check(self.value)
        return self

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Health):
            return self.value == value.value
        return self.value == value


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = Health(self, health)
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "".join(
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if not isinstance(other, Carnivore) and not other.hidden:
            other.health -= 50
