class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return "{{Name: {}, Health: {}, " \
               "Hidden: {}}}".format(self.name, self.health, self.hidden)


class Herbivore(Animal):
    def hide(self):
        if self.hidden:
            self.hidden = False
            return self.hidden
        if not self.hidden:
            self.hidden = True
            return self.hidden


class Carnivore(Animal):
    def bite(self, victim):
        if isinstance(victim, Herbivore):
            if not victim.hidden:
                victim.health -= 50
                if victim.health <= 0:
                    self.alive.pop(self.alive.index(victim))
