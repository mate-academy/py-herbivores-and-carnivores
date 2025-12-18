class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> set[str]:
        return {f"Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}"}

    def __str__(self) -> str:
        return self.__repr__()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return

        if other.hidden or other.health <= 0:
            return

        other.health -= 50

        if other.health <= 0:
            other.health = 0
            other.die()
