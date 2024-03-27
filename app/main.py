from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
        self, health: int = 100, name: str = "", hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def decrease_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    @staticmethod
    def bite(animal: "Herbivore") -> None:
        if not animal.hidden:
            animal.decrease_health(50)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
