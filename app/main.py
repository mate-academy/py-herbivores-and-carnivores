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
        return "{Name: " + f"{self.name}" + ", Health: " + \
               f"{str(self.health)}" + ", Hidden: " + \
               f"{str(self.hidden)}" + "}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(carnivore_animal: str) -> None:
        if isinstance(
                carnivore_animal, Herbivore
        ) and carnivore_animal.hidden is not True:
            carnivore_animal.health -= 50
        if carnivore_animal.health <= 0:
            Animal.alive.remove(carnivore_animal)
