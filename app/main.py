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
        res = "{Name: " + self.name + ", "
        res += "Health: " + str(self.health) + ", "
        res += "Hidden: " + str(self.hidden) + "}"

        return res


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    herbivore.alive.remove(herbivore)
