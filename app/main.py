class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, point: Herbivore) -> None:
        if point.hidden is False and isinstance(point, Herbivore) is True:
            point.health -= 50
        if point.health <= 0:
            for index, animal in enumerate(Animal.alive):
                if animal.name == point.name:
                    Animal.alive.remove(point)
