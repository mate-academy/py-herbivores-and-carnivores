class Animal:
    alive = []

    def __init__(self, name: str,  health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        animals = Animal.alive
        if not isinstance(animal, Carnivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                animals.pop(animals.index(animal))
