class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        hidden = self.hidden
        self.hidden = not hidden


class Carnivore(Animal):

    @staticmethod
    def bite(prey: Herbivore) -> None:
        if not prey.hidden and not isinstance(prey, Carnivore):
            prey.health -= 50
        if prey.health <= 0:
            prey.alive.remove(prey)
