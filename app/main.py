class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name = f"Name: {self.name}, "
        health = f"Health: {self.health}, "
        hidden = f"Hidden: {self.hidden}"
        return "{" + name + health + hidden + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if herbivore.hidden or isinstance(herbivore, Carnivore):
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.pop(Animal.alive.index(herbivore))
