class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}")


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.__class__ is Herbivore:
            if animal.hidden is False:
                animal.health -= 50
                if animal.health < 1:
                    Animal.alive.pop(Animal.alive.index(animal))


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False
