class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self._health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self._health}, Hidden: {self.hidden}}}")

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        new = max(0, min(100, value))
        self._health = new
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: Animal) -> None:
        if not target.hidden and isinstance(target, Herbivore):
            target.health = target.health - 50
