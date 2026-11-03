class Animal:
    alive = []

    def __init__(self,
                 name: str = "Unknown",
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, type(self)):
            return
        if getattr(herbivore, "hidden", False):
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            if herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
