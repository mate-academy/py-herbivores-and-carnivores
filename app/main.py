class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def die(cls, animal: str) -> None:
        cls.alive.remove(animal)


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                herbivore.die()


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

    def die(self) -> None:
        self.__class__.alive.remove(self)
