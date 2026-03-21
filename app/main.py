from __future__ import annotations


class Animal:
    alive: list[Animal] = []

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

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                if target in Animal.alive:
                    Animal.alive.remove(target)


# THIS MUST BE AT THE BOTTOM AND NOT INDENTED
def bite(target: Animal) -> None:
    for animal in Animal.alive:
        if isinstance(animal, Carnivore):
            animal.bite(target)
            break
