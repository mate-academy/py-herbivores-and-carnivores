class Animal:
    alive = []

    def __init__(self,
                 name: str, health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: "
                f"{self.name}, Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self: Animal) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health = other.health - 50
        if other.health <= 0:
            Animal.alive.remove(other)
