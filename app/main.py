class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        res = []
        for _ in self.alive:
            res.append(self.__dict__)
        return f"{res}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: object):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
