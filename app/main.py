class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        rp = f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
        return "{" + rp + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if other.health <= 0:
            other.health = 0
            Animal.alive.remove(other)
