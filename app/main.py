from typing import Union


class Animal():
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)
        print(f"{self.name} has died.")

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")

    @classmethod
    def __str__(cls) -> str:
        return f"{[list(Animal.alive)]}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden
        status = "hidden" if self.hidden else "visible"
        print(f"{self.name} is now status {status}.")


class Carnivore(Animal):

    def bite(self, herbivore: Union[Herbivore, Animal]) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)
            print(f"{self.name} bited {herbivore.name}.")
        else:
            if not isinstance(herbivore, Herbivore):
                print(f"{self.name} is cannot bite hidden {herbivore.name}.")
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")
