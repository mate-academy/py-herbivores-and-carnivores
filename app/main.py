from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " + self.name + ", Health: " + str(self.health)
            + ", Hidden: " + str(self.hidden) + "}"
        )


class Herbivore(Animal):

    def hide(self) -> None:

        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, beast: Animal) -> None:
        if isinstance(beast, Herbivore) and beast.hidden is False:

            beast.health -= 50
            if beast.health <= 0:
                Animal.alive.remove(beast)
