class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " + self.name
            + ", Health: " + str(self.health)
            + ", Hidden: " + str(self.hidden) + "}"
        )

    def __str__(self) -> str:
        return self.__repr__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health < 0:
            Animal.alive = [
                a for a in Animal.alive if a is not other
            ]
