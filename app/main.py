class AliveList(list):
    def __repr__(self) -> str:
        items = [
            f"{{Name: {animal.name}, Health: {animal.health}, Hidden: {animal.hidden}}}"
            for animal in self
        ]
        return f"[{', '.join(items)}]"


class Animal:
    alive = AliveList()

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
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            return
        if target.hidden:
            return
        target.health -= 50
