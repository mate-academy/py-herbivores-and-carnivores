from typing import Optional


class Animal:
    alive = []

    def __init__(self, name: str, health: Optional[int] = None) -> str:
        self.name = name
        self.health = health
        if self.health is None:
            self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health}, Hidden: {self.hidden}}}")

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        if self.health <= 0:
            print("Herbivore health is zero or less. Dying...")
            self.die()
            return


class Carnivore(Animal):
    def bite(self, animal: str) -> str:
        if isinstance(animal, Carnivore) or animal.hidden:
            return
        print(f"Biting {animal.name}. Health before: {animal.health}")
        animal.health -= 50
        if animal.health <= 0:
            animal.health = 0
            animal.die()
        print(f"Health after biting: {animal.health}")
