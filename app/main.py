from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: "
            + self.name
            + ", "
            + "Health: "
            + str(self.health)
            + ", "
            + "Hidden: "
            + str(self.hidden)
            + "}"
        )


class Herbivore(Animal):

    def hide(self) -> Herbivore:
        if not self.hidden:
            self.hidden = True
        elif self.hidden:
            self.hidden = False
        return self


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    Animal.alive.remove(herbivore)
