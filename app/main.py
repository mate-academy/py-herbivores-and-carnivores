class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden=False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def died(self):
        Animal.alive.remove(self)

    def __repr__(self):
        name = f"Name: {self.name}"
        health = f"Health: {self.health}"
        hidden = f"Hidden: {self.hidden}"
        return f"{{{name}, {health}, {hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore_instance: Herbivore) -> None:
        if isinstance(herbivore_instance, Herbivore)\
                and herbivore_instance.hidden is not True:
            if herbivore_instance.health > 0:
                herbivore_instance.health -= 50
            if herbivore_instance.health <= 0:
                herbivore_instance.died()
