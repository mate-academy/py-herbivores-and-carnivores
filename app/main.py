class Animal:
    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    def damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> str:

        if isinstance(herbivore, Carnivore):
            return f"{self.name} cannot bite hidden {herbivore.name}"
        if herbivore.hidden:
            return f"{self.name} cannot bite hidden {herbivore.name}"
        else:
            herbivore.damage(50)

            result = herbivore.health
            return f"{result} bite"
