class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}, Health: " \
                     f"{self.health}, Hidden: {self.hidden}" + "}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore):
        if not isinstance(herbivore, Carnivore):
            if herbivore.hidden is False:
                herbivore.health -= 50

        for i in range(len(Animal.alive)):
            if Animal.alive[i].health <= 0 and \
                    isinstance(Animal.alive[i], Herbivore):
                Animal.alive.pop(i)
