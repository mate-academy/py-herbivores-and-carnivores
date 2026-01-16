from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def is_dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return "{Name: " + str(
            self.name) + ", Health: " + str(
                self.health) + ", Hidden: " + str(self.hidden) + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.health -= 50
            victim.is_dead()
