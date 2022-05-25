class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.check_alive(self)

    @classmethod
    def check_alive(cls, self):
        if self.health <= 0 and self in cls.alive:
            cls.alive.remove(self)
        elif self.health > 0 and self not in cls.alive:
            cls.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, "\
               f"Health: {self.health}, "\
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herb: Herbivore):
        if isinstance(herb, Herbivore) and not herb.hidden:
            herb.health -= 50
            Animal.check_alive(herb)
