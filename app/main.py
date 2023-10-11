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
    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden or isinstance(herbivore, Carnivore):
            return
        herbivore.health = max(0, herbivore.health - 50)
        if not herbivore.health:
            Animal.alive.pop(Animal.alive.index(herbivore))
