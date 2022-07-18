
class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Carnivore(Animal):

    @staticmethod
    def bite(target):
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
        if target.health <= 0:
            Animal.alive.remove(target)


class Herbivore(Animal):

    def hide(self):
        # if self.hidden is True:
        #     self.hidden = False
        # else:
        #     self.hidden = True
        self.hidden = not self.hidden

# pantera = Carnivore("Bagira")
# snake = Carnivore("Kaa")
# print(Animal.alive)

# lion = Carnivore("Lion King")
# rabbit = Herbivore("Susan")
# rabbit.health == 100
# print(lion.bite(rabbit))
# rabbit.health == 50
# print(Animal.alive)


# pantera.__dict__
# snake.__dict__


# lion = Carnivore("Simba")
# len(Animal.alive[0]) == 1
# isinstance(Animal.alive, Carnivore) is True
