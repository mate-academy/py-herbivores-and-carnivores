from typing import List


class Animal:
    alive: List["Animal"] = []

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
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def die(self) -> None:
        self.health = 0
        self.hidden = True
        self.alive.remove(self)

    def bite(self, animal: object) -> None:
        pass


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            print("Error: Carnivores cannot bite other carnivores.")
        elif animal.hidden:
            print("Error: "
                  "The animal is currently hiding and cannot be bitten.")
        else:
            animal.health -= 50
            if animal.health <= 0:
                animal.die()
