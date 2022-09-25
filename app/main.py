class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self):
        name = f"Name: {self.name}"
        health = f"Health: {self.health}"
        hidden = f"Hidden: {self.hidden}"
        return f"{{{name}, {health}, {hidden}}}"


class Herbivore(Animal):
    def hide(self):
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(other: Herbivore):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50

            if other.health <= 0:
                Animal.alive.remove(other)
