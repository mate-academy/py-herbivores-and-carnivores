from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def is_alive(self) -> bool:
        if self.health <= 0:
            self.alive.remove(self)
            return False
        return True

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> int:
        if isinstance(herbivore, Herbivore)\
                and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.is_alive()
        return herbivore.health
