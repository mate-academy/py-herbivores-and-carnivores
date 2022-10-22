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

    @classmethod
    def health_control(cls, alive: list) -> object:
        for animal in alive:
            if animal.health <= 0:
                alive.remove(animal)
        return cls


class Herbivore(Animal):

    def hide(self) -> object:
        self.hidden = True if self.hidden is False else False
        return self


class Carnivore(Animal):

    def bite(self, animal: "Herbivore") -> object:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
        self.health_control(alive=self.alive)
        return self
