class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @classmethod
    def remove_animal(cls, animal: "Animal") -> None:
        cls.alive.remove(animal)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return Animal.__str__(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: "Animal") -> None:
        if animal.hidden or isinstance(animal, Carnivore):
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.remove_animal(animal)
