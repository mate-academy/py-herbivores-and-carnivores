from typing import Optional, Union


class Animal:
    alive = []

    def __init__(
        self, name: str,
            health: Optional[int] = 100,
            hidden: Optional[bool] = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

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
    def bite(self, target: Union["Herbivore", "Carnivore"]) -> None:
        if not isinstance(target, Herbivore) or target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.die()
