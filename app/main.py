class Animal:

    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden is False:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    Animal.alive.remove(herbivore)
