class Animal:
    alive = []

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return '{' + f"Name: {self.name}," \
                     f" Health: {self.health}," \
                     f" Hidden: {self.hidden}"\
               + '}'


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health == 0:
                Animal.alive.remove(other)


class Herbivore(Animal):
    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True
