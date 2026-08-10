class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self._health = 100
        self.hidden = False
        Animal.alive.append(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)
        if self._health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey):
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
