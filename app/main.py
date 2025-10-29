"""Module with classes for animals."""


class Animal:
    """A class to represent an animal.

    :param name: The name of the animal.
    :type name: str
    :param health: The health of the animal.
    :type health: int
    :param hidden: The hidden status of the animal.
    :type hidden: bool
    """

    alive: list["Animal"] = list()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        """Initializes an Animal object.

        :param name: The name of the animal.
        :type name: str
        :param health: The health of the animal.
        :type health: int
        :param hidden: The hidden status of the animal.
        :type hidden: bool
        """
        self.name = name
        self.health = health
        self.hidden = hidden
        if self not in self.__class__.alive:
            self.__class__.alive.append(self)

    def __repr__(self) -> str:
        """Return a string representation of the animal.

        :return: A string representation of the animal.
        :rtype: str
        """
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )


class Herbivore(Animal):
    """A class to represent a herbivore."""

    def hide(self) -> None:
        """Hide the herbivore."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    """A class to represent a carnivore."""

    @staticmethod
    def bite(animal: Animal) -> None:
        """Bite an animal.

        :param animal: The animal to bite.
        :type animal: Herbivore
        """
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0 and animal in animal.__class__.alive:
                animal.__class__.alive.remove(animal)
