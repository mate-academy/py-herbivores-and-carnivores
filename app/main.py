class Animal:
    alive = []

    def __new__(cls, *args, **kwargs):
        Animal.alive.append(obj := object.__new__(cls))
        return obj

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

    def __repr__(self):
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __str__(self):
        return self.__repr__()

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health > 0:
            self.__health = health
        else:
            self.__health = 0
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore) or other.hidden:
            return
        other.health -= 50
