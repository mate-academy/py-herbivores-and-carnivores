class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
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


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not herbivore.hidden and not isinstance(herbivore, Carnivore):
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
