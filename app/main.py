class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(name)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> None:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Carnivore(Animal):

    @classmethod
    def bite(cls, animal: Animal) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health == 0:
                animal.die()


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
