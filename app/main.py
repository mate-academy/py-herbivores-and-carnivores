class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        self.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if type(herbivore) is Herbivore and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
