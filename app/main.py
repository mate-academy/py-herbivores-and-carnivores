class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def __str__(self):
        return str(self.alive)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(feed):
        if isinstance(feed, Herbivore) and not feed.hidden and feed in Animal.alive:
            feed.health -= 50
            if feed.health <= 0:
                feed.die()
