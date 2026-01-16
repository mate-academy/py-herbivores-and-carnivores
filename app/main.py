from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
    self,
    name: str,
    health: int = 100,
    hidden: bool = False
) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " + self.name
            + ", Health: " + str(self.health)
            + ", Hidden: " + str(self.hidden) + "}"
        )

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, obj: Animal) -> None:
        if isinstance(obj, Herbivore) and not obj.hidden:
            obj.take_damage(50)
