class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        Name = "{Name: " + self.name
        Health = ", Health: " + str(self.health)
        Hidden = ", Hidden: " + str(self.hidden) + "}"
        return Name + Health + Hidden


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(carnivore_animal):
        if isinstance(
                carnivore_animal, Herbivore
        ) and carnivore_animal.hidden is not True:
            carnivore_animal.health -= 50
        if carnivore_animal.health <= 0:
            Animal.alive.remove(carnivore_animal)
