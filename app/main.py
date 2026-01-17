class Animal:

    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self. hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        formatted_str = (f"Name: {self.name}, "
                         f"Health: {self.health}, "
                         f"Hidden: {self.hidden}")
        return "{" + formatted_str + "}"

    def __repr__(self) -> str:
        return str(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.pop(Animal.alive.index(herbivore))
