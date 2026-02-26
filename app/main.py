from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return "[" + ", ".join(
            f'{{"Name": "{animal.name}", '
            f'"Health": {animal.health}, '
            f'"Hidden": {animal.hidden}}}'
            for animal in Animal.alive
        ) + "]"


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other: "Animal" = None) -> None:
        if other is None:
            print("You must bite an animal!")
            return

        if not isinstance(other, Herbivore):
            print("A carnivore can only eat an herbivore!")
            return

        if other.hidden:
            print(f"{other.name} is hidden, you cannot bite it!")
            return

        other.health -= 50

        if other.health <= 0:
            other.die()
