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
        Animal.add_to_alive(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}"
            f", Health: {self.health}"
            f", Hidden: {self.hidden}}}"
        )

    @classmethod
    def add_to_alive(cls, animal: Animal) -> None:
        cls.alive.append(animal)

    @classmethod
    def die(cls, animal: Animal) -> None:
        if animal.health <= 0:
            cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                super().die(animal)
