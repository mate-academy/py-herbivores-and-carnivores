class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def is_dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def bitten(self) -> None:
        self.health -= 50
        self.is_dead()


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if not isinstance(other, Herbivore) or other.hidden:
            return
        other.bitten()
