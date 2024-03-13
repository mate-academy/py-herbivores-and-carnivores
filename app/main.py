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
        Animal.alive.append(self)

    def remove_dead(self) -> None:
        Animal.alive.remove(self)

    def deadly_actions(self, bite_power: int = 50) -> None:
        self.health -= bite_power
        if self.health <= 0:
            self.remove_dead()

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(creature: Herbivore) -> None:
        if creature.hidden:
            print("Cannot bite a hidden {creature}!")
        elif isinstance(creature, Carnivore):
            print("Cannot bite another carnivore!")
        else:
            creature.deadly_actions()
