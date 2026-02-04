from typing import List


class Animal:
    alive: List["Animal"] = []  # list of all alive animals

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def take_damage(self, amount: int) -> None:
        """Reduce health by amount and remove from alive if dead."""
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        """Toggle hidden status"""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        """Bite a herbivore, reducing its health by 50 if not hidden."""
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)

        if animal.health <= 0:
            animal.health = 0
            animal.die()
