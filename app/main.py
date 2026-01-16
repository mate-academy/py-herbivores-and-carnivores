class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def _die(self) -> None:
        if self in self.__class__.alive:
            self.__class__.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other._die()
