class Animal:
    #  create list animals
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)
        # check Let’s check that the creature hasn’t died.
        self.update_status()

    def update_status(self) -> None:
        # if health <= 0 remove the animal object from Animal.alive.
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        # use magic method to get the look you want
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    """
    A method that changes animal`s hidden property
on the opposite and hides it from carnivores
    """
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    """
    A method that take herbivore object and reduces the object's health by 50.
    A method doesn't work if it's a carnivore or herbivore hiding.
    """

    @staticmethod
    def bite(herbivore_animal: Herbivore) -> None:
        if (not herbivore_animal.hidden
                and isinstance(herbivore_animal, Herbivore)):
            herbivore_animal.health -= 50
            # check if the animal is dead
            herbivore_animal.update_status()
