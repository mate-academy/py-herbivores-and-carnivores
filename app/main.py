from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> Herbivore:
        self.hidden = not self.hidden
        return self


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> Herbivore:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                Animal.die(other)
        return other
