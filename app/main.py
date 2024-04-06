from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            hidden: bool = False,
            health: int = 100
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)


class Herbivore(Animal):
    def hide (self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(self, victim: Herbivore | Carnivore) -> None:
        if isinstance(victim, Herbivore) and victim.hidden == False:
            victim.health -= 50
        if victim.health == 0:
            Animal.alive.remove(victim)

