class Animal:

    alive = list()

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, herb):
        if herb.hidden is False and isinstance(herb, Herbivore) is True:
            herb.health -= 50
        if herb.health <= 0:
            herb.alive.remove(herb)
        return herb.health
