class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

        if self.health <= 0:
            self.health = 0
            self.die()

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore) or not isinstance(animal, Herbivore):
            return

        if animal.hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()
