class Animal:
    alive = []

    def __init__(
        self,
        name: str = "",
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self._health = 0
        self.health = health
        self.name = name
        self.hidden = hidden

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value_health: int) -> None:
        self._health = value_health

        if self._health <= 0:
            Animal.alive.remove(self)
        else:
            if self not in Animal.alive:
                Animal.alive.append(self)

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
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
