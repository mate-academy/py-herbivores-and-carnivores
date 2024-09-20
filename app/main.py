class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return ("{"f"Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}""}")

    def death_check(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (isinstance(herbivore, Herbivore)
                and not herbivore.hidden):
            herbivore.health -= 50
            herbivore.death_check()
