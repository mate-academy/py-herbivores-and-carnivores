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
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    @staticmethod
    def health_control(alive: list) -> None:
        for animal in alive:
            if animal.health <= 0:
                alive.remove(animal)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Herbivore) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
        self.health_control(alive=self.alive)
