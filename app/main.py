class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    @classmethod
    def remove_animal(cls) -> None:
        for i in range(len(cls.alive)):
            if cls.alive[i].health <= 0:
                del cls.alive[i]

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if herbivore.hidden is False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            Animal.remove_animal()
