class Animal:
    alive = []

    def __init__(self, name: str):
        self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def check_alive(self):
        if self.health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def decrease_health(self, amount):
        self.health = max(0, self.health - amount)
        self.check_alive()

    def __repr__(self):
        return(f"Name: {self.name} ,"
              f"Health: {self.health} ,"
              f"Hidden: {self.hidden}" )


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.decrease_health(50)
