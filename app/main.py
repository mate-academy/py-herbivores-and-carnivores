class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        # variable 'fs' have to cut too long return-line
        fs = f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"
        return "{" + fs + "}"


class Herbivore(Animal):
    def hide(self):
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(beast):
        if not beast.hidden and isinstance(beast, Herbivore):
            beast.health -= 50
            if beast.health <= 0:
                Animal.alive.remove(beast)
