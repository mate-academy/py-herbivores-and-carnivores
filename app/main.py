class Animal:
    alive = []

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
