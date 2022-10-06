class Animal:
    alive: list = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if animal.hidden is False\
                and isinstance(animal, Herbivore) \
                and animal.health > 0:
            animal.health -= 50
            if animal.health <= 0 and animal in Animal.alive:
                Animal.alive.remove(animal)
