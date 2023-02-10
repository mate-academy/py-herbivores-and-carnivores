class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def survive_animals(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden

    def survive_animals(self):
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):

    @staticmethod
    def bite(victim):
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            victim.survive_animals()
