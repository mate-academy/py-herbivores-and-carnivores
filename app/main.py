from typing import List


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )

    @staticmethod
    def check_health(animal: "Animal") -> None:
        if animal.health <= 0:
            Animal.alive.remove(animal)

    @classmethod
    def get_alive(cls) -> List["Animal"]:
        return cls.alive


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if not (isinstance(animal, Herbivore) and not animal.hidden):
            return

        animal.health -= 50

        Animal.check_health(animal)
