class AliveList(list):
    def __repr__(self) -> str:
        return f"[{', '.join(repr(animal) for animal in self)}]"


class Animal:
    alive: list["Animal"] = AliveList()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        Animal.alive.append(self)

        if Animal.is_dead(self._health) and self in Animal.alive:
            Animal.alive.remove(self)

    @staticmethod
    def is_dead(health: int) -> bool:
        return health <= 0

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value

        if Animal.is_dead(self._health) and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore):
            return
        if other.hidden:
            return

        other.health -= 50
