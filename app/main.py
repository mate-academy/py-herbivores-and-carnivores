class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def still_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            animal.still_alive()


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
