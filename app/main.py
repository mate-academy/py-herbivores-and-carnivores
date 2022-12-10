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
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, beast: Animal) -> None:
        if isinstance(beast, Herbivore) and beast.hidden is False:
            if beast.health > 50:
                beast.health -= 50
            else:
                beast.health = 0

                for i in range(len(beast.alive)):
                    if beast.alive[i] == beast:
                        beast.alive.pop(i)
