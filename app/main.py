from __future__ import annotations


class Animal:

    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Carnivore(Animal):

    def bite(self, target: str = "Herbivore") -> None:
        if isinstance(target, Herbivore):
            if not target.hidden :
                target.health -= 50
                if target.health <= 0 and target in Animal.alive:
                    Animal.alive.remove(target)


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
