class Animal:
    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        animal.health -= 50
        if animal.health <= 0 and animal in Animal.alive:
            Animal.alive.remove(animal)
