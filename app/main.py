

class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health : int = health
        self.hidden : bool = False
        if self.health > 0:
            Animal.alive = Animal.alive + [self]

    def __str__(self) -> str:
        return (
            "{Name: "
            + self.name
            + ", Health: "
            + str(self.health)
            + ", Hidden: "
            + str(self.hidden)
            + "}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
