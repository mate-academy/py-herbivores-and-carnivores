from typing import List, Type

class Animal:
    alive: List['Animal'] = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        """Remove the animal from the alive list if its health is 0 or below."""
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        """Return a string representation of the animal in the required format."""
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle the hidden status of the herbivore."""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Type[Animal]) -> None:
        """
        Bite another animal. If the target is a herbivore and not hidden,
        decrease its health by 50. If health drops to 0 or below, the animal dies.
        """
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()
        elif isinstance(other, Carnivore):
            print("Carnivores do not bite each other.")
        elif other.hidden:
            print(f"{other.name} is hidden and cannot be bitten.")


# Example usage
if __name__ == "__main__":
    lion = Carnivore("King Lion")
    panther = Carnivore("Bagira")
    rabbit = Herbivore("Susan")

    print(Animal.alive)
