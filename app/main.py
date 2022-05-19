class Animal:
    alive = []

    def __repr__(self):
        return "{" + f"Name: {self.name}," \
                     f" Health: {self.health}," \
                     f" Hidden: {self.hidden}" + "}"

    def __init__(self, name, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):

    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if not other.health:
                Animal.alive.remove(other)
