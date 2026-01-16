class Animal:
    """
    Parent class of animals.
    """
    alive = []  # Class attribute to keep track of all alive animals

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def remove_dead(cls) -> None:
        """
        Removes dead animals from alive attribute
        :return: None
        """
        # Removes any dead animals from the alive list
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    def __repr__(self) -> str:
        # String representation for the alive list
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        """
        Hides animal from carnivores.
        :return:
        """
        # Change the hidden attribute to the opposite value
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        """
        Bites other herbivore animal and takes his health down.
        :param herbivore: Herbivore - animal to be bitten
        :return: None
        """
        # Check if the target is a Herbivore and not hidden
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            # Remove herbivore from the alive list if its health reaches zero
            if herbivore.health <= 0:
                Animal.remove_dead()
