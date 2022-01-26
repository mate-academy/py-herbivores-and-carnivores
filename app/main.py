class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(herbivor_obj):
        if not isinstance(herbivor_obj, Carnivore) \
                and herbivor_obj.hidden is False:
            herbivor_obj.health -= 50
        if herbivor_obj.health == 0:
            Animal.alive.remove(herbivor_obj)
