from typing import Any

class AnimalList(list):
    def __repr__(self) -> str:
        items = []
        for animal in self:
            items.append(
                f"{{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(items) + "]"


class AnimalMeta(type):
    def __setattr__(cls, name: str, value: Any) -> None:
        if name == "alive" and not isinstance(value, AnimalList):
            value = AnimalList(value)
        super().__setattr__(name, value)


class Animal(metaclass=AnimalMeta):
    alive: AnimalList = AnimalList()

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)
