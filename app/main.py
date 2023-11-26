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
        res = f"{{Name: {self.name}, "
        res += f"Health: {self.health}, "
        res += f"Hidden: {self.hidden}}}"

        return res


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.alive.remove(herbivore)
