class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.is_alive()

    def __repr__(self):
        return f'{{Name: {self.name}, ' \
               f'Health: {self.health}, ' \
               f'Hidden: {self.hidden}}}'

    def is_alive(self):
        Animal.alive.append(self)
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(prey):
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health = prey.health - 50

        if prey.health <= 0:
            Animal.alive.remove(prey)
