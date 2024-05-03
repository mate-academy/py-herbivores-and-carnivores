from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def decrease_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.die()

    def toggle_hidden(self) -> None:
        self.hidden = not self.hidden

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health"
                f": {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.toggle_hidden()


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.decrease_health(50)
