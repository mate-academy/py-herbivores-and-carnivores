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
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @staticmethod
    def del_dead_animal() -> None:
        animals = Animal.alive.copy()
        for animal in animals:
            if animal.health <= 0:
                del Animal.alive[Animal.alive.index(animal)]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    bite_damage = 50

    def bite(self, animal: Animal) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= self.bite_damage

            Animal.del_dead_animal()
