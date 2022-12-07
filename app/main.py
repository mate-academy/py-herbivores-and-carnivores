class Animals:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animals.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animals):

    def hide(self) -> Animals:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False
        return self


class Carnivore(Animals):

    def bite(self, animal: Animals) -> Animals:
        if isinstance(animal, Carnivore) or animal.hidden is True:
            return animal
        animal.health -= 50
        if animal.health <= 0:
            Animals.alive.remove(animal)
        return animal
