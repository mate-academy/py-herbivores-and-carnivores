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
        return ("{Name: " + self.name
                + ", Health: " + str(self.health)
                + ", Hidden: " + str(self.hidden) + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
                if animal.health <= 0:
                    del Animal.alive[Animal.alive.count(animal)]
