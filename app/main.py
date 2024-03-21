class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        symbol_right = "}"
        symbol_left = "{"
        return (f"{symbol_left}Name: {self.name}, "
                f" Health: {self.health}, "
                f" Hidden: {self.hidden}{symbol_right}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, other: "Herbivore") -> None:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
