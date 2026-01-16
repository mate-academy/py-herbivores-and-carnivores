class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if not self.hidden else False
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        if herbivore.hidden is False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50

        if herbivore.health <= 0:
            self.alive.remove(herbivore)
