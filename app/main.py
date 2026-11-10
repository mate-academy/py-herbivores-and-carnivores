from typing import ClassVar


class AliveList(list):
    def __repr__(self) -> str:
        items = [
            f"{{Name: {animal.name}, Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        ]
        return f"[{', '.join(items)}]"


class Animal:
    alive: ClassVar[AliveList] = AliveList()

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        if not isinstance(Animal.alive, AliveList):
            Animal.alive = AliveList(Animal.alive)

        self.name = name
        self.hidden = hidden
        self.health = health

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0:
            if self in Animal.alive:
                Animal.alive.remove(self)
        else:
            if self not in Animal.alive:
                Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if self.health == 0:
            return
        if target.hidden or target.health == 0:
            return
        if isinstance(target, Herbivore):
            target.health -= 50

