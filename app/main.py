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
        name = f"Name: {self.name}, "
        health = f"Health: {self.health}, "
        hidden = f"Hidden: {self.hidden}"
        return "{" + name + health + hidden + "}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if self.hidden is False else False
        return self.hidden


class Carnivore(Animal):
    def bite(self, victim):
        if not isinstance(victim, Carnivore) and victim.hidden is False:
            self.__sub__(victim)
