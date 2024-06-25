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
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(other: Animal) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            if other.health <= 50:
                Animal.alive.remove(other)
            else:
                other.health -= 50
