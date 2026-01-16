class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
        else:
            print(f"{self.name} cannot bite hidden {other.name}")
        if other.health <= 0:
            self.__class__.alive.pop(self.__class__.alive.index(other))


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
