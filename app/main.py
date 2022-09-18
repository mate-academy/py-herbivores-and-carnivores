class Animal:
    alive = []

    def __new__(cls, *args, **kwargs):
        cls.alive.append(obj := object.__new__(cls))
        return obj

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        if health > 0:
            self.__health = health
        else:
            self.__health = 0
            self.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore) or other.hidden:
            return
        other.health -= 50
