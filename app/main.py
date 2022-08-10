class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.health = health
        self.name = name
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self):
        return "{" + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other):
        if isinstance(other, Carnivore) or other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other.__class__.alive.remove(other)
