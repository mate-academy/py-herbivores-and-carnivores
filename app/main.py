class Animal:
    alive = list()

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        self.alive.append(self)

    def __repr__(self) -> str:
        return ("{"
                + f"Name: {self.name}, "
                + f"Health: {self.health}, "
                + f"Hidden: {self.hidden}"
                + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal) -> None:
        if not (isinstance(other, Carnivore) or other.hidden):
            other.health = max(other.health - 50, 0)
            if other.health == 0:
                Animal.alive.remove(other)
