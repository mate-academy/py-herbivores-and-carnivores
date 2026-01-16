from typing import List


class Animal:
    alive : List["Animal"] = []

    def __init__(self, name : str, health : int = 100) -> None:
        self.name : str = name
        self.health : int = health
        self.hidden : bool = False
        if self.health > 0:
            Animal.alive = Animal.alive + [self]

    def __str__(self) -> str:
        result = ("{Name: "
                  + str(self.name)
                  + ", Health: "
                  + str(self.health)
                  + ", Hidden: "
                  + str(self.hidden) + "}")
        return result

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb : Herbivore) -> None:
        if not herb.hidden and isinstance(herb, Herbivore):
            herb.health -= 50
            if herb.health <= 0:
                Animal.alive.remove(herb)
