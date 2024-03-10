from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
        target.die()


if __name__ == "__main__":
    rabbit = Herbivore("Susan", 50)
    lion = Carnivore("Simba")
    lion2 = Carnivore("King Lion")

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    print(rabbit.health)
    lion.bite(rabbit)
    print(rabbit.health)  # bited

    # rabbit.hide()
    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health)  # lion cannot bite hidden rabbit

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health) == 0  # rabbit is dead

    print(rabbit in Animal.alive)  # False
    for animal in Animal.alive:
        print(animal)
