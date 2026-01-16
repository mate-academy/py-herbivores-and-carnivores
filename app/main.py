class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    def alive_animal(self, damage: str) -> str:
        self.health -= damage
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> str:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: str) -> str:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.alive_animal(50)
