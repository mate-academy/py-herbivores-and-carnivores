from __future__ import annotations


class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        animals = {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }
        return f"{animals}".replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = self.hidden is False


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if victim.hidden is False and isinstance(victim, Herbivore):
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)
