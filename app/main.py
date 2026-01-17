class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> Animal:
        self.hidden = not self.hidden
        return self


class Carnivore(Animal):

    def bite(self, animal: Animal) -> Animal:
        if isinstance(animal, Carnivore) or animal.hidden is True:
            return animal
        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
        return animal
