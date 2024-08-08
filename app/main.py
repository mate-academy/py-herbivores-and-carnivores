class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Carnivore(Animal):

    @classmethod
    def bite(cls, animal: Animal) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                animal.die()


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
