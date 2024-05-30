from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.if_alive(self)

    @classmethod
    def if_alive(cls, beast: Animal) -> None:
        cls.alive += [beast] if beast.health > 0 else []

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, beast: Animal) -> None:
        if isinstance(beast, Herbivore) and beast.hidden is False:
            beast.health -= 50
        Animal.alive.remove(beast) if beast.health <= 0 else []
