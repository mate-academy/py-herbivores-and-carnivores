from __future__ import annotations


class Animal:
    alive = list()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.born_animal(self)

    @classmethod
    def born_animal(cls, animal: Animal) -> None:
        cls.alive.append(animal)

    @classmethod
    def die(cls, animal: Animal) -> None:
        cls.alive.remove(animal)

    def get_bited(self) -> None:
        self.health -= 50
        if self.health <= 0:
            self.die(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if not prey.hidden and isinstance(prey, Herbivore):
            prey.get_bited()
