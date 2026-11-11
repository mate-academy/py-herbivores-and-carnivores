class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if (
            not other.hidden
            and other.health > 0
            and isinstance(other, Herbivore)
        ):
            other.health -= 50

        if (
            other.health <= 0
            and other in Animal.alive
            and isinstance(other, Herbivore)
        ):
            Animal.alive.remove(other)
