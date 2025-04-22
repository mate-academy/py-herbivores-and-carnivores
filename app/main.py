class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f""
                f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if other.hidden is not True and isinstance(other, Herbivore):
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
