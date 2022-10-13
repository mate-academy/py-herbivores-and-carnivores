class Animal:
    live = []

    def __init__(self, name, health = 100, hidden = False) -> None:
        self.health = health
        self.hidden = hidden
        self.name = name
        self.__class__.live.append(self)
    
    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    
    def hide(self):
        self.hidden = True

class Carnivore(Animal):

    def bite(self, ):
