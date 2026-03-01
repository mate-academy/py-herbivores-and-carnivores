from typing import List, Any


class Animal:
    alive: List[Any] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def _check_death(self) -> None:
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Any) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()
        elif isinstance(target, Carnivore):
            print(f"{self.name} не може кусати іншого хижака!")
        elif target.hidden:
            print(f"{target.name} надійно сховався!")
