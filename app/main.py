class Animal:
    alive = list()

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
        return (
            "{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is not True else False


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
