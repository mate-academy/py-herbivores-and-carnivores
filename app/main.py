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
        animal_name = f"Name: {self.name}"
        animal_health = f"Health: {self.health}"
        animal_hidden = f"Hidden: {self.hidden}"
        return f"{{{animal_name}, {animal_health}, {animal_hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(eaten_animal: Animal) -> None:
        if not eaten_animal.hidden and isinstance(eaten_animal, Herbivore):
            eaten_animal.health -= 50
        if eaten_animal.health <= 0:
            Animal.alive.remove(eaten_animal)
