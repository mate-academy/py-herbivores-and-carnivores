from pycodestyle import continued_indentation


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, other):
        if  other.hidden == False and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)



