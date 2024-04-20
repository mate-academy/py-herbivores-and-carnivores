class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        if self. hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(another_animal: Animal) -> None:
        if (isinstance(another_animal, Herbivore)
                and another_animal.hidden is not True):
            another_animal.health -= 50
        if another_animal.health <= 0:
            Animal.alive.remove(another_animal)
