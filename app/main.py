class Animal:
    live = []

    def __init__(self,
                 name: str,
                 health: int = 100) -> None:
        self.health = health
        self.hidden = False
        self.name = name
        Animal.live.append(self)

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
        if herbivore.hidden is False\
                and isinstance(herbivore, Herbivore) \
                and herbivore.health > 0:
            herbivore.health -= 50
            if herbivore.health <= 0 and herbivore in Animal.alive:
                Animal.alive.remove(herbivore)
