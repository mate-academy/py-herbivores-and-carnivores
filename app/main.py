from __future__ import annotations


class Animal:
    """
    Base class for all animals. Stores common attributes and registers
    every created instance in the global list of alive animals.

    :param name: animal's name
    :param health: starting health value (default: 100)
    :param hidden: visibility flag, determines if
    animal is hiding (default: False)
    """

    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:

        self.health = health
        self.name = name
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        """
        Returns string representation of the animal instance.

        :return: formatted string with name, health and hidden status
        """
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _is_alive(self) -> bool:
        """
        Checks whether the animal is still alive.

        :return: True if health is above 0, otherwise False
        """
        return self.health > 0

    def _die(self) -> None:
        """
        Removes the animal from the global 'alive' list.
        Used when health reaches zero or below.

        :return: None
        """
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    """
    Herbivore class representing plant-eating animals.
    Provides ability to hide from carnivores.
    """

    def hide(self) -> None:
        """
        Toggles hidden state for the herbivore.
        When hidden, carnivores cannot attack it.

        :return: None
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    Carnivore class representing predators.
    Carnivores can attack herbivores, reducing their health by 50.
    Hidden herbivores and other carnivores cannot be attacked.

    """

    # noinspection PyMethodMayBeStatic
    def bite(self, target: Herbivore) -> None:
        """
        Performs a bite attack on the target herbivore.
        The attack deals 50 damage only when:
         - the target is a Herbivore
         - the target is not hidden

        Once the target's health reaches zero or below,
        it is removed from the global list of alive animals.

        :param target: Herbivore instance to attack
        :return: None
        """
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50

            if not target._is_alive():
                target._die()
