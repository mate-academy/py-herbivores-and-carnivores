from __future__ import annotations


class Animal:
    alive = list()

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        me = f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
        return "{" + me + "}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = bool(int(self.hidden) - 1)


class Carnivore(Animal):

    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)
