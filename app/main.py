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
        return "{Name: " + self.name + ", Health: " \
               + str(self.health) + ", Hidden: " + str(self.hidden) + "}"


class Herbivore(Animal):

    def hide(self) -> bool:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False
        return self.hidden


class Carnivore(Animal):

    def bite(self, prey: Herbivore) -> int:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        if prey.health <= 0:
            self.alive.remove(prey)
        return prey.health
