class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def _die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            f"}}"
        )

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        # can only bite herbivores
        if not isinstance(other, Herbivore):
            return

        # cannot bite hidden herbivores
        if other.hidden:
            return

        other.health -= 50

        if other.health <= 0:
            other.health = 0
            other._die()
