class Animal:

    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False) -> None:

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

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore):
        herbivore.health -= (50 if isinstance(herbivore, Herbivore) and
                             herbivore.hidden is False else 0)
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
