class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> repr:
        name = f"Name: {self.name}, "
        health = f"Health: {self.health}, "
        hidden = f"Hidden: {self.hidden}"
        return "{" + name + health + hidden + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
