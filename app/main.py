class Animal:
    alive = []
    hidden = False

    def __init__(self, name: str, heals: int = 100) -> None:

        self.name = name
        self.health = heals
        Animal.alive.append(self)

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
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health < 1:
                Animal.alive.pop(Animal.alive.index(animal))
