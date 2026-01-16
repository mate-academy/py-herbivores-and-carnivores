from __future__ import annotations


class AliveList(list):

    def __str__(self: AliveList) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"

    # def __repr__(
    #         self: AliveList[Animal]
    # ) -> str:
    #     return str(Animal.get_alive_status())

# def print(alive: Animal.alive) -> None:
#     print(Animal.get_alive_status())


class Animal:
    alive: AliveList = AliveList()

    def __init__(
            self: Animal,
            name: str,
            health:
            int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self: Animal) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self: Animal,
            herbivore: Herbivore
    ) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0 and herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
