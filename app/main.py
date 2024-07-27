class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 hidden: bool = False,
                 health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def dying(self) -> alive:
        if self.health <= 0:
            return Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        target.health -= 50
        target.dying()
