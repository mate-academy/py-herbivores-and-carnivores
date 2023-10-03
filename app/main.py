class Animal:
    """
    Represents a basic Animal creature, stores all its instances.

    Attributes:
    ----------
    name : str
        the name of the animal
    health : int
        the health points of the animal
    hidden : bool
        the hiding status of the animal
    """

    alive = list()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f""
                f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    """
    Represents a Herbivore animal.

    Attributes:
    ----------
    name : str
        the name of the animal
    health : int
        the health points of the animal
    hidden : bool
        the hiding status of the animal

    Methods:
    -------
    hide()
        Switches the "hidden"
        attribute of the animal to the opposite value.
    """

    def hide(self) -> None:
        """
        Switches the "hidden" attribute of the animal to the opposite value.
        :return: None
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
        Represents a Carnivore animal.

        Attributes:
        ----------
        name : str
            the name of the animal
        health : int
            the health points of the animal
        hidden : bool
            the hiding status of the animal

        Methods:
        -------
        bite()
            Takes a Herbivore instance and decreases its "health"
            attribute by 50 pts.
        """

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        """
        Takes a Herbivore instance and decreases its "health"
        attribute by 50 pts.
        Removes the Herbivore instance out of "Animal.alive"
        class attribute if its "health" <= 0.
        The method does not work against another Carnivore instance,
        or if the Herbivore's "hidden" attribute is currently True.
        :param herbivore: Herbivore, mandatory
            A Herbivore instance
        :return: None
        """
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
        if isinstance(herbivore, Herbivore) and herbivore.health <= 0:
            Animal.alive.remove(herbivore)
