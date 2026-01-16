class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f'{{'f'Name: {self.name}, ' \
               f'Health: {self.health}, ' \
               f'Hidden: {self.hidden}}}'


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(prey):
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)
