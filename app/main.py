class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


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
            other.die()
