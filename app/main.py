class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def __remove__(self):
        for animal in self.alive:
            if animal.health <= 0:
                self.alive.remove(animal)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if other.hidden is False and not isinstance(other, Carnivore):
            other.health -= 50
        super().__remove__()
