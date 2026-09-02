class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

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
    def bite(self, herbivore: Herbivore) -> str:
        if isinstance(herbivore, Carnivore):
            return f"{self.name} cannot bite {herbivore.name}"
        if herbivore.hidden is True:
            return f"{self.name} cannot bite hidden {herbivore.name}"
        else:
            herbivore.health -= 50
            if herbivore.health <= 0:
                self.alive.remove(herbivore)
            return "bited"
