class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):








