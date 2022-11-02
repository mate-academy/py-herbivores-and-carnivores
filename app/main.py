class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: float = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}," \
                     f" Health: {self.health}," \
                     f" Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, name_of_herbivore: Herbivore) -> None:
        if isinstance(name_of_herbivore, Herbivore) and \
                name_of_herbivore.hidden is False:
            name_of_herbivore.health -= 50
            if name_of_herbivore.health <= 0:
                Animal.alive.remove(name_of_herbivore)
