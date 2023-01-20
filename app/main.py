class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden is False and\
                herbivore.__class__ is not self.__class__:
            herbivore.health -= 50
            herbivore.hidden = False
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
