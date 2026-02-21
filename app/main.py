from typing import List, Dict, Optional


class Animal:
    alive = []  # Class attribute to keep track of all living animals

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name: str = name  # Animal's name
        self.health: int = health  # Animal's health (default is 100)
        self.hidden: bool = hidden  # Whether the animal is hiding (default is False)
        Animal.alive.append(self)  # Add this animal to the alive list

    def __str__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"  # String representation of the animal

    def __repr__(self) -> str:
        return self.__str__()  # This ensures that the __repr__ method works as expected

    @classmethod
    def remove_dead(cls) -> None:
        """Removes dead animals from the alive list."""
        cls.alive = [animal for animal in cls.alive if animal.health > 0]  # Filter out dead animals


class Herbivore(Animal):
    def hide(self) -> None:
        """Changes the 'hidden' property to the opposite value."""
        self.hidden = not self.hidden  # Toggle the hidden state


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        """Bites the herbivore and decreases its health by 50, if possible."""
        if isinstance(target, Herbivore):  # Ensure the target is a Herbivore
            if not target.hidden:  # If the target is not hiding
                target.health -= 50  # Reduce target's health by 50
            # If the herbivore's health goes to 0 or below, it will be removed by remove_dead
            elif target.hidden:  # If the herbivore is hiding
                return  # Do nothing if the herbivore is hiding
        # Call remove_dead() after a bite to ensure dead animals are removed
        Animal.remove_dead()
