class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal_to_bite: Animal) -> None:
        if (isinstance(animal_to_bite, Herbivore)
                and not animal_to_bite.hidden):
            animal_to_bite.health -= 50
            if animal_to_bite.health <= 0:
                Animal.alive.remove(animal_to_bite)
