class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> list:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, bitten_animal: "Animal") -> None:
        if isinstance(bitten_animal, Herbivore):
            if bitten_animal.hidden is False:
                bitten_animal.take_damage(50)
