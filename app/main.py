class Animal:
    health = 100
    hidden = False
    alive = []

    def __init__(self, *args) -> None:
        self.name = args
class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, object: Herbivore) -> None:
        if self.hidden is False:
            object.health = object.health / 2

