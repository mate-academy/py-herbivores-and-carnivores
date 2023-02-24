class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        result = (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )

        return result

    def __repr__(self) -> str:
        result = (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )

        return result


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = not self.hidden
        else:
            self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50

        if other.health <= 0:
            Animal.alive.remove(other)
