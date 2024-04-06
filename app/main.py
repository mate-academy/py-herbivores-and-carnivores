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

    def __repr__(self) -> str:
        return ("{{Name: {name},"
                " Health: {health},"
                " Hidden: {hidden}}}".format(name=self.name,
                                             health=self.health,
                                             hidden=self.hidden))


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not herbivore.hidden and not isinstance(herbivore, Carnivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
