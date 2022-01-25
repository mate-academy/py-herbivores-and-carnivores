class Animal:
    alive = []

    def __init__(self, name):
        self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, "\
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, victim):
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)
