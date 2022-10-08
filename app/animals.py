from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = 0 if health <= 0 else health
        self.hidden = False

        if self.health > 0:
            self.add_born(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}" + "}"

    @staticmethod
    def add_born(animal: Animal) -> None:
        Animal.alive.append(animal)

    @staticmethod
    def remove_dead(animal: Animal) -> None:
        for index in range(len(Animal.alive)):
            if animal is Animal.alive[index]:
                Animal.alive.pop(index)


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                if other.health <= 0:
                    other.health = 0
                    other.remove_dead(other)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True
