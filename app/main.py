class Animal:

    alive = []
    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health <= 0:
            self._health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
