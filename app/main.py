from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

    @classmethod
    def dead_animal(cls, animal: Animal) -> None:
        cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        bite_damage = 50
        is_herbivore = isinstance(herbivore, Herbivore)

        if not herbivore.hidden and (herbivore.health > 0) and is_herbivore:
            if herbivore.health <= bite_damage:
                Animal.dead_animal(herbivore)

            herbivore.health -= bite_damage
