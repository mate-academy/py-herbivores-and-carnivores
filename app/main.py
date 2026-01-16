class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):

        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def if_alive(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):
    @staticmethod
    def bite(opponent):
        if isinstance(opponent, Herbivore) and not opponent.hidden:
            opponent.health -= 50
            opponent.if_alive()
