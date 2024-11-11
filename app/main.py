class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            return Animal.alive.append(self)

    def remove_animal_list(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
            f"Health: {self.health}, " \
            f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, animal: Herbivore, damage: int = 50) -> None:

        if self.__class__ != animal.__class__:
            if animal.hidden is False:
                animal.health -= damage

                if animal.health <= 0:
                    animal.remove_animal_list()
