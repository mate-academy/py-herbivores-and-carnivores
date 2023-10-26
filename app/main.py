class Animal:
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    alive = []

    def __str__(self):
        return self.name

    def check_is_alive(self):
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(another_beast):
        if isinstance(another_beast, Carnivore) or another_beast.hidden:
            return "Can`t bit an another beast"
        else:
            another_beast.health -= 50
            another_beast.check_is_alive()
