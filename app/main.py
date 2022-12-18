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
        Animal.alive.append(self)

    def __sub__(self, other: int) -> Animal:
        self.health -= other
        return self

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}," \
                     f" Health: {self.health}," \
                     f" Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                for index, beast in enumerate(Animal.alive):
                    if beast is animal:
                        del Animal.alive[index]
