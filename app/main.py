from typing import Type


class Animal:
    alive: list[Type["Animal"]] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return str([repr(animal) for animal in cls.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if not isinstance(prey, Herbivore):
            return
        if prey.hidden:
            return

        prey.health -= 50
        if prey.health <= 0:
            prey.die()
