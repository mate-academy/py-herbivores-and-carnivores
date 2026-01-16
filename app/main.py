class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self._health = None
        self.hidden = hidden
        self.health = health

    @property
    def health(self) -> None:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)

        if self._health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)
        else:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
