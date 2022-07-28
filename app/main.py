class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self):
        return '{' + 'Name: {}, Health: {}, Hidden: {}'.\
               format(self.name, self.health, self.hidden) + '}'


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        is_herbivore = isinstance(animal, Herbivore) and animal in self.alive

        if is_herbivore and not animal.hidden:
            animal.health -= 50

            if animal.health <= 0:
                self.alive.remove(animal)
