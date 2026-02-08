class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = str(name)
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal):

        if herbivore.hidden == False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
