class Animal:
    alive = []

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"

    def check_if_dead(self):

        if self in self.alive and self.health <= 0:
            self.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            animal.check_if_dead()
