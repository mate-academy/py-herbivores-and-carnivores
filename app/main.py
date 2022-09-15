class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return "{{Name: {0}, Health: {1}, Hidden: {2}}}".format(
            self.name, self.health, self.hidden)


class Herbivore(Animal):

    def hide(self):
        self.hidden = False if self.hidden else True


class Carnivore(Animal):

    def bite(self, other_animal):
        if not isinstance(other_animal, Carnivore) and not other_animal.hidden:
            other_animal.health -= 50
            if other_animal.health <= 0:
                other_animal.health = 0
                i = self.__class__.alive.index(other_animal)
                self.__class__.alive.pop(i)
