class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if not prey.hidden and isinstance(prey, Herbivore):
            prey.health -= 50
        if prey.health <= 0:
            self.alive.remove(prey)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
