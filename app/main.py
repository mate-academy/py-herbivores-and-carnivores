from __future__ import annotations

class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str
    ) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def _check_death(
            self,
    ) -> None:
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    class Herbivore(Animal):
        def hide(
                self,
        ) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(
            self,
            target: Animal
    ) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            target._check_death()

