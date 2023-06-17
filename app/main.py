from __future__ import annotations


class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore_obj: Herbivore | Carnivore) -> None:
        if isinstance(herbivore_obj, Herbivore) and \
                herbivore_obj.hidden is False:
            herbivore_obj.health -= 50
            if herbivore_obj.health <= 0:
                self.alive.remove(herbivore_obj)
