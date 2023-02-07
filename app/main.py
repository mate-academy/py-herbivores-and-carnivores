from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.add_to_alive(self)

    def __str__(self) -> str:
        return "{" + \
               f"Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}" \
               + "}"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def add_to_alive(cls, obj: Animal) -> None:
        cls.alive.append(obj)

    @staticmethod
    def remove_from_alive(animal: Animal) -> None:
        Animal.alive = list(filter(lambda x: x != animal, Animal.alive))


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if not isinstance(other, Herbivore):
            return
        if not other.hidden:
            other.health -= 50
        if other.health <= 0:
            self.remove_from_alive(other)
