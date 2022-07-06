class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        status = f"Name: {self.name}, "\
            f"Health: {self.health}, "\
            f"Hidden: {self.hidden}"\

        return f"{{{status}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    def bite(self, prey: Herbivore):
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50

        if prey.health <= 0:
            Animal.alive.remove(prey)
