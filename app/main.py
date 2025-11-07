class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.hidden = hidden
        self._health = 0
        Animal.alive.append(self)
        self.health = health  # через setter

    def __repr__(self):
        # так список распечатает ровно нужную строку
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        v = max(0, int(value))
        self._health = v
        if v == 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal):
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health = other.health - 50
