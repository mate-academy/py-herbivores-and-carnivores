class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def __str__(cls):
        return "[" + ", ".join(repr(animal) for animal in cls.alive) + "]"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
