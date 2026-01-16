from typing import ClassVar


class AnimalList(list):
    def __repr__(self) -> str:
        # Represent as list of dicts with desired fields
        return repr([
            {
                "name": animal.name,
                "health": animal.health,
                "hidden": animal.hidden,
            }
            for animal in self
        ])


class Animal:
    alive: ClassVar[AnimalList] = AnimalList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        state = "hidden" if self.hidden else "visible"
        print(f"{self.name} is now {state}")


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()


if __name__ == "__main__":
    lion = Carnivore("Simba")
    assert len(Animal.alive) == 1
    assert isinstance(Animal.alive[0], Carnivore)

    rabbit = Herbivore("Susan", 25)
    rabbit.hide()
    assert rabbit.hidden is True

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    assert rabbit.health == 100

    lion.bite(rabbit)
    assert rabbit.health == 50

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 50

    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 0
    assert rabbit not in Animal.alive

    panther = Carnivore("Bagheera")
    snake = Carnivore("Kaa")

    print(Animal.alive)  # This will print the custom formatted list of dicts
