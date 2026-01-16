class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name = name
        self._health = 0
        self.health = health
        self.hidden = False

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        old_health = self.health
        self._health = max(0, value)

        if old_health > 0 and self._health == 0:
            if self in Animal.alive:
                Animal.alive.remove(self)
        elif old_health == 0 and self._health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if (
            isinstance(target, Herbivore)
            and not target.hidden
            and target in Animal.alive
        ):
            target.health = max(0, target.health - 50)
