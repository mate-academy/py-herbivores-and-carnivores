class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False

        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        # можно кусать только травоядных и только если они не спрятаны
        if not isinstance(other, Herbivore):
            return

        if other.hidden:
            return

        other.health -= 50

        if other.health <= 0:
            other.die()
