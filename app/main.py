class Animal:
    alive = []  # Class attribute to keep track of all living animals

    def __init__(self, name):
        self.name = name
        self.health = 100
        self._hidden = False  # Hidden attribute is private
        Animal.alive.append(self)  # Add to the list of living animals

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target):
        if isinstance(target, Herbivore) and not target.hidden and target in Animal.alive:
            target.health -= 50
            if target.health <= 0:
                target.health = 0
                Animal.remove_dead()