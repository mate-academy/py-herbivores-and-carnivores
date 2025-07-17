from typing import ClassVar, List


class Animal:
    alive: ClassVar[List["Animal"]] = []
    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)
    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore):
            return
        if herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
