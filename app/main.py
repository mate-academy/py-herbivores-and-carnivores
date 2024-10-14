class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self._hidden: bool = False
        Animal.alive.append(self)

    @property
    def hidden(self) -> bool:
        return self._hidden

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def __sub__(self, damage: int) -> None:
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.die()

    def hide(self) -> None:
        self._hidden = not self._hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health = max(0, herbivore.health - 50)
            if herbivore.health == 0:
                herbivore.die()
