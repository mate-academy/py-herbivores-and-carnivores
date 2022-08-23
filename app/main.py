class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __remove__(self):
        for animal in self.alive:
            if animal.health <= 0:
                self.alive.remove(animal)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, other):
        if other.hidden is False and not isinstance(other, Carnivore):
            other.health -= 50
        super().__remove__()
