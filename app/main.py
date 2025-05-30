class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.health = 100
        self.name = name
        self.hidden = False
        self.alive.append(self)

class Herbivore(Animal):
    def hide(self):
       pass
