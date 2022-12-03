class Animal:
    alive = []

    def __init__(self, name: str,

                 health: int = 100,

                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, prey: Herbivore) -> int:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        if prey.health <= 0:
            self.alive.remove(prey)
        return prey.health
