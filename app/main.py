class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
