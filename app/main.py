from typing import ClassVar, override


class Animal:
    alive: ClassVar[list["Animal"]] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.health: int = health
        self.name: str = name
        self.hidden: bool = hidden
        Animal.alive.append(self)

    @override
    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"  # noqa: E501


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden: bool = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if target.hidden or isinstance(target, Carnivore):
            return
        target.health -= 50

        if target.health <= 0:
            Animal.alive.remove(target)
