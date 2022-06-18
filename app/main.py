class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    Animal.alive.pop(
                        Animal.alive.index(herbivore)
                    )
