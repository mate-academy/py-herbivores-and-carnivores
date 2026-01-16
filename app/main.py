from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return f"{{Name: {self.name}," \
            f" Health: {self.health}, Hidden: {self.hidden}}}"

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) \
                and not prey.hidden \
                and prey in Animal.alive:
            prey.health -= 50
            if prey.health <= 0:
                prey.health = 0
                Animal.alive.remove(prey)
