class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False)\
            -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def __getattr__(self, item: list) -> list:
        return [alive_animal for alive_animal in self.alive]


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Herbivore) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                self.alive.pop(self.alive.index(animal))
