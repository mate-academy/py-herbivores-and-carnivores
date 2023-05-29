from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {str(self.hidden)}}}"
        )

    def die(self) -> None:
        self.__class__.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: "Herbivore") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()
