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

        if self.health > 0:
            self.__class__.alive.append(self)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb: Herbivore) -> None:
        if isinstance(herb, Herbivore) and not herb.hidden:
            herb.health -= 50
            if herb.health <= 0:
                try:
                    self.__class__.alive.remove(herb)
                except ValueError:
                    pass
