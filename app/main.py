class Animal:
    alive = []

    def __init__(self, name: str, *args) -> None:
        self.name = name
        self.health = 100 if args == () else args[0]
        self.hidden = False
        Animal.alive.append(self)

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
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
