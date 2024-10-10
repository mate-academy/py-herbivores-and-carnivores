class Animal:
    alive = []

    def __init__(self, name: "str", health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def die(animal: "Animal") -> None:
        if animal in Animal.alive:
            Animal.alive.remove(animal)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.die(herbivore)
