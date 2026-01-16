from typing import List, Union


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Union[Herbivore, "Carnivore"]) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.die()
