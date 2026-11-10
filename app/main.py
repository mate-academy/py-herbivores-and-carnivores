class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )

    def __str__(self) -> str:
        return self.__repr__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden or target not in Animal.alive:
            return

        target.health -= 50

        if target.health <= 0:
            target.health = 0
            Animal.alive.remove(target)
