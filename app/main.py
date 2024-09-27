class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        name = self.name
        health = self.health
        hidden = self.hidden
        return f'{{Name: {name}, Health: {health}, Hidden: {hidden}}}'


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(feed):
        if isinstance(feed, Herbivore) and not feed.hidden:
            feed.health -= 50
            if feed.health <= 0:
                Animal.alive.remove(feed)
