class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if animal.hidden is False and not isinstance(animal, Carnivore):
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
