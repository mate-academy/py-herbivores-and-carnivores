class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def remove_from_alive(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            animal.remove_from_alive()
