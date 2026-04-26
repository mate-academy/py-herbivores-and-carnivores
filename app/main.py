class Animal:

    alive: list[Animal] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")

    __repr__ = __str__

    def damage(self, damage_amount: int) -> None:
        self.health -= damage_amount
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return
        if isinstance(animal, Herbivore):
            if animal.hidden:
                return
            else:
                animal.damage(50)


if __name__ == "__main__":
    lion = Carnivore("Simba")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    print(Animal.alive)
