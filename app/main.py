class Animal:
    alive: list["Animal"] = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        inner = (
            ", ".join(f"{k.title()}: {v}" for k, v in self.__dict__.items())
        )
        return f"{{{inner}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)
