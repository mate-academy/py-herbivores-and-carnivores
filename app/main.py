class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @staticmethod
    def is_dead(name: str) -> None:
        if name.health <= 0:
            Animal.alive.remove(name)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(name: Herbivore) -> None:
        if isinstance(name, Herbivore) and not name.hidden:
            name.health -= 50
            name.is_dead(name)
