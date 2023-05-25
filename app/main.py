class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return f"\u007bName: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}\u007d"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health = max(other.health - 50, 0)
        if other.health == 0:
            self.__class__.alive.remove(other)
