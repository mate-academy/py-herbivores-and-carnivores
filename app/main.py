class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.add_alive()

    def add_alive(self) -> None:
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)
        elif self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return (f"Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}")

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:

        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
        animal.add_alive()
