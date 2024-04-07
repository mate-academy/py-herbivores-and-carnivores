class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self):
        Animal.alive.remove(self)


class Herbivore(Animal):
    def __init__(self, name, health=100, hidden=False):
        super().__init__(name, health, hidden)

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target):
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.die()
