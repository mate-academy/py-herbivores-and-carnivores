class Animal:
    alive = []

    def __init__(
        self, name: str, health: str = 100, hidden: bool = False
    ) -> None:
        self.hidden = hidden
        self.health = health
        self.name = name
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            for index, animals in enumerate(Animal.alive):
                if animal == animals:
                    Animal.alive.pop(index)
