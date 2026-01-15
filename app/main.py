class Animal:

    alive: list = []

    def __init__(self, name: str, health: int = 100) -> None:

        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)
        else:
            self.health = 0

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def check_health(self) -> None:

        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:

        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: Animal) -> None:

        if isinstance(target, Carnivore) or target.hidden:
            return
        target.health -= 50
        target.check_health()
