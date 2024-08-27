class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"\u007bName: {self.name}, "
                + f"Health: {self.health}, Hidden: {self.hidden}\u007d")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not (isinstance(herbivore, Carnivore) or herbivore.hidden):
            herbivore.health -= 50

            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
