from typing import List, Optional


class Animal:
    alive: List["Animal"] = []

    def __init__(self,
                 name: Optional[str] = None,
                 health: int = 100,
                 hidden: bool = False,
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self not in Animal.alive and self.health > 0:
            Animal.alive.append(self)
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other: "Herbivore") -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0 and other in Animal.alive:
                Animal.alive.remove(other)
