class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: None) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
                if animal.health <= 0:
                    if animal in Animal.alive:
                        Animal.alive.remove(animal)
