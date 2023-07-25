from typing import List


class Animal:
    """
    Class representing an animal.
    """
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        """
        Initialize an animal with a name and health.
        """
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        """
        Represent the animal as a string.
        """
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def check_health(self) -> None:
        """
        Check the health of the animal.
        If the health is 0 or less, remove the animal from the alive list.
        """
        if self.health <= 0:
            self.__class__.alive.remove(self)


class Herbivore(Animal):
    """
    Class representing a herbivore, which is a type of animal.
    """

    def hide(self) -> None:
        """
        Change the hidden status of the herbivore.
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    Class representing a carnivore, which is a type of animal.
    """

    def bite(self, other: "Herbivore") -> None:
        """
        Bite another herbivore, decreasing its health by 50.
        If the other animal is not a herbivore or is hidden, do nothing.
        """
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other.check_health()
