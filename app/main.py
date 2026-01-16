from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int | None = 100) -> None:
        self.name, self.health, self.hidden = name, health, False
        self.add_animal(self)

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.delete_animal(self)

    @classmethod
    def add_animal(cls, new_animal: Animal) -> None:
        cls.alive.append(new_animal)

    @classmethod
    def delete_animal(cls, new_animal: Animal) -> None:
        if new_animal in cls.alive:
            del cls.alive[cls.alive.index(new_animal)]

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not bool(self.hidden)


class Carnivore(Animal):
    @staticmethod
    def bite(hunted_animal: Animal) -> None:
        if (
            not isinstance(hunted_animal, Carnivore)
            and not hunted_animal.hidden
        ):
            hunted_animal.take_damage(50)
