from __future__ import annotations


class AliveList(list):
    def __repr__(self) -> str:
        return str([
            {
                "Name": animal.name,
                "Health": animal.health,
                "Hidden": animal.hidden,
            }
            for animal in self
        ])


class Animal:
    alive: AliveList = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden: bool = False
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

        if isinstance(target, Carnivore):
            return

        if target.hidden:
            return

        target.health -= 50
        if target.health <= 0:
            target.health = 0
            Animal.alive.remove(target)
