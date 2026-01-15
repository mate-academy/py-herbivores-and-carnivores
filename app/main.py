from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        self.on_set_health()

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def on_set_health(self) -> None:
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)
        elif self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, beast: Animal) -> None:
        if (not isinstance(beast, Herbivore)
                or beast.hidden
                or beast not in Animal.alive):
            return

        beast.health -= 50
        beast.on_set_health()
