
class Animal:

    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            pass

        elif animal.hidden is True:
            messsage = f"{self} cannot bite hidden {animal}"
            return messsage

        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50

            if animal.health <= 0:
                messsage = f"{animal} is dead"
                Animal.alive.remove(animal)
                return messsage
