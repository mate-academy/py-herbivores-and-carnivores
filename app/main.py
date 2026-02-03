class Animal:
    alive: list["Animal"] = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore_animal: Animal) -> None:
        if (isinstance(herbivore_animal, Carnivore)
                or herbivore_animal.hidden is True):
            return
        herbivore_animal.health -= 50
        if herbivore_animal.health <= 0:
            Animal.alive.remove(herbivore_animal)


if __name__ == "__main__":
    lion = Carnivore("Lion")
    zebra = Herbivore("Zebra")
    lion.bite(zebra)
