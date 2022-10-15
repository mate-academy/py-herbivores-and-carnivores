class Animal:
    live = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.hidden = hidden
        self.name = name
        self.__class__.live.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0 and herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
