class Animal():
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other_animal: Animal) -> None:
        if isinstance(other_animal, Herbivore) and not other_animal.hidden:
            other_animal.health -= 50
            if other_animal.health < 1:
                Animal.alive.remove(other_animal)
                other_animal.health = 0
