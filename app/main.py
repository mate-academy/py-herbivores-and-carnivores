class Animal:
    """
    Base class for herbivores and carnivores.

    Attributes:

        name (str): The animal's name.

        health (int): Health level, default 100.

        hidden (bool): Indicates whether the animal is hidden, default False.

        alive (list["Animal"]): Class attribute that stores all live instances.
    """
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {
            self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    """
    A subclass of Animal representing a prey animal.
    """

    def hide(
            self
    ) -> None:
        """
        Toggle the animal's hidden status to protect it from carnivores.
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    A subclass of Animal representing a hunting animal.
    """

    def bite(
            self,
            target: Animal
    ) -> None:
        """
        Attempt to bite another animal.

        The attack only succeeds if the target is an instance of Herbivore
        and is not currently hiding. If the target's health reaches 0,
        it is removed from the Animal.alive registry.

        Args:
            target (Animal): The animal object to be attacked.
        """
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
