from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, *args, **kwargs) -> None:
        if args:
            self.health = args[0]
        else:
            self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def decrease_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Herbivore | Carnivore) -> None:
        if isinstance(target, Carnivore) or target.hidden:
            return

        target.decrease_health(50)
