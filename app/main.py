class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False) -> None:
        self.name = name
        self._health = None
        self.health = health
        self.hidden = hidden

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)

        if self._health == 0:
            if self in self.__class__.alive:
                self.__class__.alive.remove(self)
        else:
            if self not in self.__class__.alive:
                self.__class__.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if (
            isinstance(target, Herbivore)
            and not target.hidden
            and target in self.__class__.alive
        ):
            target.health -= 50