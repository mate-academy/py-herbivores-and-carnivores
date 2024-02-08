class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            healt: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = healt
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}"
            f"}}"
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
