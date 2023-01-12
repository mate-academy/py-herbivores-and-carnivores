class Animal:

    alive = list()

    def __init__(self, name: str, health:int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Herbivore) -> None:
        if animal.hidden is False and type(animal) != Carnivore:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
