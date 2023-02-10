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

    def __repr__(self):
        return '{'f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}"'}'

    @classmethod
    def if_death(cls, animal):
        if animal.health <= 0:
            Animal.alive.remove(animal)


class Herbivore(Animal):

    def hide(self):
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, animal: Animal):
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50

        Animal.if_death(animal)
