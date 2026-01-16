class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:

        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50

        if herbivore.health < 1:
            del Animal.alive[Animal.alive.index(herbivore)]
