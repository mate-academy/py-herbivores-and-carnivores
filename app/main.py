from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health : int = 100, hidden: bool = False) \
            -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @property
    def is_alive(self):
        return self.health == 0

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name == "health":
            if value == 0 and self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.health = max(victim.health - 50, 0)
