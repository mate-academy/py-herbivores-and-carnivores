from __future__ import annotations


class Animal:
    health = 100
    hidden = False
    alive = []

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name
        if len(args) == 1:
            self.health = args[0]
        elif len(args) == 2:
            self.health = args[0]
            self.hidden = args[1]
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{"\
               + f"Name: {self.name}," \
                 f" Health: {self.health}," \
                 f" Hidden: {self.hidden}"\
               + "}"


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if victim.hidden is False and victim.__class__ is Herbivore:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
