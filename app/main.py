from typing import Any


class Animal:
    class AliveList(list):
        def __repr__(self) -> str:
            return str([repr(animal) for animal in self])

    alive = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Any) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                if other in Animal.alive:
                    Animal.alive.remove(other)
