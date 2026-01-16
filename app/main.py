class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)
        self.dead_remove()

    def dead_remove(self) -> None:
        for animal in self.alive:
            if animal.health < 1:
                self.alive.remove(animal)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(animal: type) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden is False:
                animal.health -= 50
            Animal.dead_remove(animal)
