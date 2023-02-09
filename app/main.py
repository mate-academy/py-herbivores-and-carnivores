from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        tp = self
        return f"{{Name: {tp.name}, Health: {tp.health}, Hidden: {tp.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Herbivore | Carnivore) -> None:
        if isinstance(victim, Herbivore):
            if not victim.hidden:
                victim.health -= 50
                if victim.health <= 0:
                    Animal.alive.remove(victim)
