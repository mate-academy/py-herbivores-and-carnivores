class Animal:
    alive = []

    def __init__(
        self,
        name,
        health=100,
        hidden=False,
    ):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"Name: {self.name}, Health: {self.health}, Hidden: {str(self.hidden)}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target):
        if isinstance(target, Herbivore) and not target.hidden:
            target.health = max(0, target.health - 50)
            if target.health == 0 and target in Animal.alive:
                Animal.alive.remove(target)
