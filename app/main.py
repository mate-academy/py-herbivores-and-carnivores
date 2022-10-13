class Animal:
    live = []

    def __init__(self, name, health = 100, hidden = False):
        self.health = health
        self.hidden = hidden
        self.name = name
        self.__class__.live.append(self)


class Herbivore(Animal):
    
    def hide(self):
        self.hidden = True

class Carnivore(Animal):

    def bite(self, ):
