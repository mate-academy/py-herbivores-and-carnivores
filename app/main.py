class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __str__(self):
        return self.__repr__()


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal):
        if isinstance(other, Carnivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health < 0:
            Animal.alive = [a for a in Animal.alive if a is not other]
