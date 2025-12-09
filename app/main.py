class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self,value):
        self._health = value
        if self._health <= 0:
            self._health = 0
            self.die()

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
