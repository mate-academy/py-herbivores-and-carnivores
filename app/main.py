class AliveAnimals(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive = AliveAnimals()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbi: Herbivore) -> None:
        if not isinstance(herbi, Herbivore) or herbi.hidden:
            return
        herbi.health -= 50
