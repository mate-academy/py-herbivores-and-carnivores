class Animal:
    alive = []
    def __init__(self, name: str, hidden: bool = False):
        self._health = 100
        self.name = name
        self.hidden = hidden
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self._health}, Hidden: {self.hidden}}}"

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self,value: int):
        new = max(0, min(100, value))
        self._health = new
        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target):
        if not target.hidden and isinstance(target, Herbivore) and target.health > 0:
            target.health = target.health - 50
        if target.health <= 0 and target in Animal.alive:
            Animal.alive.remove(target)