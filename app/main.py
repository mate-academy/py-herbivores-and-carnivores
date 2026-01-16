class Animal:
    """stores all alive animals"""
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        """Changes the hidden property of the beast to the opposite value"""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> None:
        """Takes a herbivore object and decreases the object's health by 50,
        does not work if it is another сarnivore,
        or the herbivore is currently hiding"""
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
