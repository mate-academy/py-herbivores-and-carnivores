class Animal:

    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __sub__(self, other):
        other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)

    def __repr__(self):
        return f"{{Name: {self.name}," \
            f" Health: {self.health}," \
            f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if self.hidden is False else False
        return self.hidden


class Carnivore(Animal):
    def bite(self, victim):
        if not isinstance(victim, Carnivore) and victim.hidden is False:
            self.__sub__(victim)
