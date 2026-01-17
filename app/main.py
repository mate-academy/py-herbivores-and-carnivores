class Animal:
    """
    Represents an animal entity with attributes for its name,
    health, and visibility state. It manages a shared
    class-level collection of all living animals and provides
    methods for its representation and lifecycle, like marking
    an animal as dead. This class is designed for use in contexts where
    managing entities with health and visibility properties is required.

    """
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        """
        Initializes an instance of the class with the
        specified parameters, sets
        default values for health and hidden if not provided,
        and appends the instance to the 'alive' collection.

        :param name: The name of the instance being created.
        :type name: str
        :param health: The health value of the instance.
            Defaults to 100.
        :type health: int
        :param hidden: A flag indicating whether the instance
            is hidden. Defaults to False.
        :type hidden: bool
        """
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        """
        Generate a string representation of the object,
        including its name, health,
        and hidden status in a formatted way.

        :return: A string containing the object's name,
            health, and hidden status.
        :rtype: str
        """
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        """
        Marks the instance as deceased by removing
        it from the list of living animals.

        This method checks if the current instance
        is part of the global list of living
        animals and removes it if it exists.

        :return: None
        """
        if self in Animal.alive:
            self.__class__.alive.remove(self)


class Herbivore(Animal):
    """
    Represents a herbivorous animal that inherits
    from the Animal class.

    This class includes functionality specific to
    herbivores, including an ability to hide, by
    toggling a state that determines whether the
    herbivore is hidden or visible.

    """
    def hide(self) -> None:
        """
        Toggles the hidden state of an object.

        This method changes the value of the `hidden`
        attribute to its opposite state. If `hidden`
        is True, it will become False, and vice versa.

        :return: None
        """
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    Represents a carnivorous animal that inherits
    from the Animal class.

    This class includes functionality specific to
    carnivores, including an ability to attack
    herbivorous animals through biting, which
    reduces the target's health and can potentially
    cause death.

    """
    def bite(self, other: Herbivore) -> None:
        """
        Attacks a herbivorous animal by reducing its health.

        This method allows a carnivore to bite a herbivore,
        dealing 50 points of damage. The attack only works
        if the target is a herbivore and is not currently
        hidden. If the herbivore's health drops to 0 or below
        after the attack, the animal dies and is removed
        from the list of living animals.

        :param other: The herbivorous animal to be attacked.
        :type other: Herbivore
        :return: None
        """
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.health = 0
                other.die()
