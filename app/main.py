class Animal:
    """
    Base class for herbivores and carnivores.

    Attributes:

        name (str): The animal's name.

        health (int): Health level, default 100.

        hidden (bool): Indicates whether the animal is hidden, default False.

        alive (list): Class attribute that stores all live instances.
    """
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{self.name}"


class Herbivore(Animal):
    """
    A subclass of Animal representing a prey animal.
    """

    def hide(self) -> None:
        """
        Toggle the animal's hidden status to protect it from carnivores.
        """
        self.hidden = not self.hidden
