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
        if isinstance(self, Animal):
            return f"{{Name: {
                self.name
            }, Health: {self.health}, Hidden: {self.hidden}}}"
        else:
            return str(self)


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if all(
            (
                isinstance(target, Herbivore),
                target in Animal.alive,
                not target.hidden
            )
        ):
            target.health -= 50
        if target.health <= 0:
            target.health = 0
            Animal.alive.remove(target)


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
