class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(pray):
        if isinstance(pray, Herbivore) and pray.hidden is False:
            pray.health -= 50
            pray.die()
