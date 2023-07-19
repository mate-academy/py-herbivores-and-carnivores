from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}"

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def is_hiding(self) -> bool:
        return self.hidden

    @staticmethod
    def remove_dead_animals() -> None:
        Animal.alive = [animal for animal in Animal.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden  # Toggle the value of 'hidden'
        if self.hidden:
            print(f"{self.name} is now hiding.")
        else:
            print(f"{self.name} is no longer hiding.")


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Carnivore) and not herbivore.is_hiding():
            herbivore.health -= 50
            print(
                f"{self.name} bit {herbivore.name}. "
                f"{herbivore.name} health: {herbivore.health}"
            )
            if herbivore.health <= 0:
                print(f"{herbivore.name} is dead.")
                Animal.remove_dead_animals()
        else:
            print(f"{self.name} cannot bite {herbivore.name}.")
