class Animal:
    alive = []

    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(beast: Herbivore):
        if isinstance(beast, Herbivore) and beast.hidden is False:
            beast.health -= 50
            if beast.health <= 0:
                Animal.alive.remove(beast)
