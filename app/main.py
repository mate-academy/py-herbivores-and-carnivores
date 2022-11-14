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
        return "Name: {name}, Health: {health}, Hidden: {hidden}".format(
            name=self.name, health=self.health, hidden=self.hidden
        )

    def __repr__(self) -> str:
        return "{{Name: {name}, Health: {health}, Hidden: {hidden}}}".format(
            name=self.name, health=self.health, hidden=self.hidden
        )


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50

        if other.health <= 0:
            Animal.alive.remove(other)
