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
        return "{" + f"Name: {self.name}, " \
                     f"Health: {self.health}, " \
                     f"Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50

            for i in Animal.alive:
                if i.name == herbivore.name:
                    i.health = herbivore.health
                    if i.health <= 0:
                        Animal.alive.remove(i)
