class Animal:
    alive = []

    def __init__(self, name, health: int = 100):
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        info = f"Name: {self.name}, "\
            f"Health: {self.health}, "\
            f"Hidden: {self.hidden}"\

        return f"{{{info}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore):
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50

            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
