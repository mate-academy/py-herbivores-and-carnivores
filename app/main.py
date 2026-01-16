from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def is_alive(self) -> bool:
        return self.health > 0

    def handle_death(self) -> None:
        if self.is_alive() is False:
            Animal.alive.remove(self)
            print(f"{self.name} is dead")

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if victim.hidden is False and isinstance(victim, Herbivore):
            victim.health -= 50
            victim.handle_death()
