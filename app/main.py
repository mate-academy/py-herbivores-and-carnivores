class Animal:
    alive = []

    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, " f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return str(self)

    def decrease_health(self, amount) -> None:
        self.health = max(0, self.health - amount)

        if self.health == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.decrease_health(50)
