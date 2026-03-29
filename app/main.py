class Animal:
    alive = []

    def __init__(self, name, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        return self


class Carnivore(Animal):
    def bite(self, herbivore):
        if herbivore.hidden is False \
                and herbivore in Animal.alive \
                and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                Animal.alive.remove(herbivore)
        return self
