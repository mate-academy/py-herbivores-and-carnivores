from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health : int = 100, hidden: bool = False ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def is_alive(self) -> bool:
        if self.health <= 0:
            Animal.alive.remove(self)
            return False
        return True

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True

class Carnivore(Animal):

    @staticmethod
    def bite(victim: Animal):
        if not victim.hidden and not isinstance(victim, Carnivore):
            victim.health -= 50
            victim.is_alive()

