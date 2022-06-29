class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return "{Name: " + self.name + \
               ", Health: " + str(self.health) + \
               ", Hidden: " + str(self.hidden) + "}"


class Herbivore(Animal):

    def hide(self):
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(victim):
        if not isinstance(victim, Carnivore):
            if not victim.hidden:
                victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)
