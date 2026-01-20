class Animal:
    alive = []

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

    def __str__(self) -> str:
        return (
            "{"
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )

    def __repr__(self) -> str:
        return str(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, new_health: int) -> None:
        if new_health > 0:
            self._health = new_health
        else:
            self._health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden and other in Animal.alive:
                other.health -= 50
