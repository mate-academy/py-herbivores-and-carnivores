class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False):
        self.health = health
        self.name = name
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore):
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
            if herbivore.health <= 0:
                self.__class__.alive.remove(herbivore)
