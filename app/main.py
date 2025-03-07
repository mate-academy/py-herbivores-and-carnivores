class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self):
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self):
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
