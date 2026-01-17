from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self._hidden = False
        Animal.alive.append(self)

    @property
    def hidden(self) -> bool:
        return self._hidden

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f""
                f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self._hidden = not self._hidden


class Carnivore(Animal):

    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                prey.die()
