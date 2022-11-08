class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        result = f"Name: {self.name}, Health: {self.health}, " \
                 f"Hidden: {self.hidden}"
        return "{" + result + "}"


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
                    Animal.alive.remove(herbivore)
