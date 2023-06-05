class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
